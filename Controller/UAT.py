# Import all packages used
import sys
import time
from time import sleep
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.uic import loadUi
import pandas as pd
import socket
import requests
import modelBuilder as mb
import initialize
import webbrowser


#This worker class can be run as a seperate thread when run inside the GUI. This way the Model and listiner can run symultaniously with the GUI
class Worker(QObject):
    
    #QuestionLabelText is global so the GUI can change depending on the model
    global QuestionLabelText
    #signals are used to communicate with functions int the GUI class below
    nextQSig = pyqtSignal()  # give worker class a finished signal
    incorrect = pyqtSignal()  # give worker class a finished signal

    def __init__(self, nextQ, questionDifficulty, distributions, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # provide a bool run condition for the class
        
        #these initialze the model info
        self.nextQ = nextQ
        self.questionDifficulty = questionDifficulty
        self.distributions = distributions
        self.QuestionLabelText = nextQ
        
        # finds the questions index so we can remove it from the viable questions later
        self.lastQ_index = self.questionDifficulty[self.questionDifficulty['problem'] == self.nextQ].index[0]
        
        
        #the do_work function is called to begin the model and communicate with 
    def do_work(self):
        #creates a socket s, This is for communications between the AutoGrader
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 5555
        #binds the socket to the correct port
        try:
            s.bind((host, port))
        except socket.error as es:
            print(str(es))
        #begins listining for the autograder
        s.listen(1)   
        #initializes data collection df for the model
        columns = ["student_id", "problem","timestamp","graded","score","sourcehash"]
        attempt = pd.DataFrame(columns = columns)
        global attemptNum
        attemptNum = 1
        
        print("waiting")

        #this loop is essentially
        #1. connect to autograder
        #2. wait for submission from autograder
        #3. pull any submissions from the last ~second
        #4. confirm the submission is the correct one
        #5. if submission is =100 continue, else back to 2
        #6. model go brrrr
        #7. back to 2
        
        while (self.continue_run):
            
            # waits for notification from autograder, then fetches new submission 
            conn, addr = s.accept()
            print(f"conn from {addr}")
            tmsg = conn.recv(1024)
            umsg = conn.recv(1024)
        
            timestamp = tmsg.decode("utf-8")
            username = umsg.decode("utf-8")


            course = "1"
            
            time.sleep(0)
            
            API_Response = requests.get("https://tutor.dfcs-cloud.net/api/v1/getSubmissionHistory.php?apiKey=dfcs_capstone&course=" + course + "&problem=" + self.nextQ + "&start="+ timestamp, timeout = 3)

            response = API_Response.json()  #full resonse from API
            submissions = response.get("submissions")   #list of submissions
            num_submissions = response.get("size")  #number of submissions in 'submissions'


                    #check if there is more than one submission
            if num_submissions == 1:
                submission = submissions.get("0")
            elif num_submissions == 0:
                print("no submission recieved, check internet and try again")
            else :
                for j in num_submissions :
                    submission = submission.get("j")
                    if (submission.get("user_name") == username):
                        break
                    
            #else if more submissions check usernames

            print(submission)
            
            #clean data for the model
            submission.pop("user_name")
            responseSeries = pd.Series(submission)
            attempt = attempt.append(responseSeries, ignore_index=True)

            if submission["score"] == "100":                
                # once they get a 100, clean up their response data df                
                attempt.graded = attempt.graded.astype(int)
                attempt.score = attempt.score.astype(float)
                qData = mb.convertRawtoClean(attempt)
                
                #using that data, determine the next question
                self.nextQ = mb.nextQuestion(self.nextQ, self.questionDifficulty, self.distributions, qData)
                
                # drop that previous question from the viable questions
                self.questionDifficulty = self.questionDifficulty.drop([self.lastQ_index]).reset_index().drop(["index"], axis=1)

                # now finds the next questions index so it can later drop it from viable Qs
                self.lastQ_index = self.questionDifficulty[self.questionDifficulty['problem'] == self.nextQ].index[0]

                # find the python file with that question name then open it
                path = "..\Labs\\" + self.nextQ + ".py"
                webbrowser.open(path)


                # reset attempt and submission
                attempt = pd.DataFrame(columns = columns)
                submission = ""

                # gives the GUI the next question name
                self.QuestionLabelText = self.nextQ
                
                # resets attempt number
                attemptNum = 1
                self.nextQSig.emit()
                
            else:

                attemptNum = attemptNum + 1
                self.incorrect.emit()
                
    
    def stop(self):
        self.continue_run = False  # set the run condition to false on stop
        print("tutorOff")


#this class is the GUI that we run the worker class in.
class Gui(QWidget):

    stop_signal = pyqtSignal()  # make a stop signal to communicate with the worker in another thread
    global QuestionLabelText

    def __init__(self, nextQ, questionDifficulty, distributions):
        super(Gui, self).__init__()
        loadUi(NextQScreen, self)
        
        # initializes the dfs, next question, and number of questions
        self.nextQ = nextQ
        self.questionDifficulty = questionDifficulty
        self.dummyQuestionDifficulty = questionDifficulty
        self.distributions = distributions
        self.numQs = int(len(questionDifficulty))
        
        # if we choose to hide the difficulty, this will ensure it doesnt show up
        if not showDifficulty:
            self.DifficultyLabel.hide()
        
        # displays intial GUI screen and buttons
        self.initUI()
        self.DecreaseButton.clicked.connect(self.decrease)
        self.IncreaseButton.clicked.connect(self.increase)
        self.MaintainButton.clicked.connect(self.maintain)
    
    
    def decrease(self):
        """
        Once someone clicks the "Decrease Difficulty" button, this finds the 
            decreased-difficulty next problem
        """
        self.findProblem("decrease")


    def increase(self):
        """
        Once someone clicks the "Increase Difficulty" button, this finds the 
            increased-difficulty next problem
        """
        self.findProblem("increase")
        

    def maintain(self):
        """
        Once someone clicks the "Maintain Difficulty" button, this finds the 
            maintained-difficulty next problem
        """
        self.findProblem("maintain")


    def findProblem(self, direction):
        """
        Finds the next problem based on the direction given

        Parameters
        ----------
            direction : str
                direction in which to change difficulty
        """
        # finds the last question's index for dropping purposes
        self.lastQ_index = self.questionDifficulty[self.questionDifficulty['problem'] == self.nextQ].index[0]
        
        # changes the problem difficulty according to the direction given
        if direction == "decrease":
            self.worker.QuestionLabelText = mb.reduceDifficulty(self.worker.QuestionLabelText, self.questionDifficulty)
        elif direction == "increase":
            self.worker.QuestionLabelText = mb.increaseDifficulty(self.worker.QuestionLabelText, self.questionDifficulty)
        else:
            self.worker.QuestionLabelText = mb.maintainDifficulty(self.worker.QuestionLabelText, self.questionDifficulty)

        # removes that question from the viable Qs
        self.questionDifficulty = self.questionDifficulty.drop([self.lastQ_index]).reset_index().drop(["index"], axis=1)
        
        # determines how that problem ranks overall then displays problem in GUI and opens file
        self.nextQ = self.worker.QuestionLabelText
        self.rank = int(self.questionDifficulty.index[self.questionDifficulty.problem == self.nextQ][0])
        self.QuestionNameLabel.setText(self.worker.QuestionLabelText)
        self.path = "..\Labs\\" + self.nextQ + ".py"
        webbrowser.open(self.path)
        
        # puts the problem description into the GUI
        try:
            textPath = "..\Labs\QuestionText\\" + self.worker.QuestionLabelText + ".html"
            questionHtml = open(textPath, 'r', encoding='utf-8')
            questionText = questionHtml.read()
            self.QuestionTextLabel.setText(questionText)
        except:
            textPath = "..\Labs\QuestionText\ErrorText.html"
            questionHtml = open(textPath, 'r', encoding='utf-8')
            questionText = questionHtml.read()
            self.QuestionTextLabel.setText(questionText)
        
        # Labels the problem with some necessary info and helpful words of encouragement
        if direction == "decrease":
            self.CorrectLabel.setText("This one should be a little easier!")
        elif direction == "increase":
            self.CorrectLabel.setText("This one should be a little harder!")
        else:
            self.CorrectLabel.setText("This one should be similar in difficulty!")
        self.IncorrectLabel.setText("")
        self.AttemptLabel.setText("Attempt Number: " + str(1))
        self.DifficultyLabel.setText("Difficult: " + str(self.rank) + " out of " + str(self.numQs))
        self.update


    def initUI(self):

        sleep(.1)

        #creates a thread
        self.thread = QThread()
        #creates a worker class
        self.worker = Worker(self.nextQ, self.questionDifficulty, self.distributions)
        #moves the worker to the thread we created
        self.worker.moveToThread(self.thread)
        #Binds the worker "do_work" function to the thead starting
        self.thread.started.connect(self.worker.do_work)
        #connects the "NextQuestion" function to the nextQSig signal
        self.worker.nextQSig.connect(self.NextQuestion)
        #Same thing but inccorect
        self.worker.incorrect.connect(self.IncorrectUpdate)
        #starts the thread and in turn the "do_work"function of the worker class
        self.thread.start()
        #erases question Text Label
        self.QuestionTextLabel.setText("")
    
        #Checks to see if the html for our question exists
        #if not throw errortext.html
        self.nextQ = QuestionLabelText
        try:
            textPath = "..\Labs\QuestionText\\" + QuestionLabelText + ".html"
            questionHtml = open(textPath, 'r', encoding='utf-8')
            questionText = questionHtml.read()
            self.QuestionTextLabel.setText(questionText)
        except:
            textPath = "..\Labs\QuestionText\ErrorText.html"
            questionHtml = open(textPath, 'r', encoding='utf-8')
            questionText = questionHtml.read()
            self.QuestionTextLabel.setText(questionText)

        #initializes labels
        self.QuestionNameLabel.setText(QuestionLabelText)
        self.rank = int(self.dummyQuestionDifficulty.index[self.dummyQuestionDifficulty.problem == QuestionLabelText][0])
        self.DifficultyLabel.setText("Difficult: " + str(self.rank) + " out of " + str(self.numQs))
        self.IncorrectLabel.setText("")
        self.CorrectLabel.setText("")
        self.AttemptLabel.setText("Attempt Number: " + "1")
        #Show GUI
        self.show()
    
    #updates GUI in case of incorrect attempt
    def IncorrectUpdate(self):
        self.IncorrectLabel.setText("Incorrect, try again bud")
        self.CorrectLabel.setText("")
        self.AttemptLabel.setText("Attempt Number: " + str(attemptNum))
        self.DifficultyLabel.setText("Difficult: " + str(self.rank) + " out of " + str(self.numQs))
        self.update
    
    #updates GUI with new qusetion in case of correct attempt
    def NextQuestion(self):
        self.QuestionNameLabel.setText(self.worker.QuestionLabelText)
        self.rank = int(self.dummyQuestionDifficulty.index[self.dummyQuestionDifficulty.problem == self.worker.QuestionLabelText][0])
        
        try:
            textPath = "..\Labs\QuestionText\\" + self.worker.QuestionLabelText + ".html"
            questionHtml = open(textPath, 'r', encoding='utf-8')
            #all the extra breaks at the end are to fix a problem where the question text was being cut off
            questionText = questionHtml.read() + "<br><br><br><br><br><br><br><br><br>"
            self.QuestionTextLabel.setText(questionText)
        except:
            textPath = "..\Labs\QuestionText\ErrorText.html"
            questionHtml = open(textPath, 'r', encoding='utf-8')
            questionText = questionHtml.read()
            self.QuestionTextLabel.setText(questionText)
        
        self.CorrectLabel.setText("Great Job! Try this one")
        self.IncorrectLabel.setText("")
        self.DifficultyLabel.setText("Difficult: " + str(self.rank) + " out of " + str(self.numQs))
        self.AttemptLabel.setText("Attempt Number: " + str(attemptNum))
        self.update



#MAIN
if __name__ == '__main__':
    # Change to True if you want to show the difficulty in the GUI
    showDifficulty = False
    
    #initializes model dat and the nextQ
    global QuestionLabelText, nextQ, questionDifficulty, distributions
    nextQ, questionDifficulty, distributions = initialize.initialize()
    
    #initializes the GUI and its given problem and opens the problem
    QuestionLabelText = nextQ
    path = "..\Labs\\" + nextQ + ".py"
    webbrowser.open(path)
    NextQScreen = "../View/NextQOutputScreen.ui"
    
    #starts app
    app = QApplication(sys.argv)
    gui = Gui(nextQ, questionDifficulty, distributions)
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")
