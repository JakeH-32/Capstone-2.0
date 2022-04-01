import sys
import time

from time import sleep

# from PyQt6.uic import loadUi

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets

from datetime import datetime
import time
import pandas as pd
import socket
import numpy as np
import datetime
import sys
import requests
import json
import threading
import modelBuilder as mb
import initialize
import webbrowser



# QuestionLabelText = "Problem #1"
LinkToCanvas="<a href=\"https://canvas.instructure.com/courses/4116250\">'Click here to go to Canvas Page'</a>"
class Worker(QObject):

    global QuestionLabelText
    nextQSig = pyqtSignal()  # give worker class a finished signal
    incorrect = pyqtSignal()  # give worker class a finished signal

    def __init__(self, nextQ, questionDifficulty, distributions, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # provide a bool run condition for the class
        self.nextQ = nextQ
        self.questionDifficulty = questionDifficulty
        self.distributions = distributions
        self.QuestionLabelText = nextQ
        self.lastQ_index = self.questionDifficulty[self.questionDifficulty['problem'] == self.nextQ].index[0]
        
        
    def do_work(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        host = socket.gethostname()
        port = 5555
        
        try:
            s.bind((host, port))
        except socket.error as es:
            print(str(es))
        
        s.listen(1)   

        columns = ["student_id", "problem","timestamp","graded","score","sourcehash"]
        attempt = pd.DataFrame(columns = columns)
        i = 1
        print("waiting")
        global attemptNum
        attemptNum = 1
        while (self.continue_run):
            
            # waits for notification from autograder, then fetches new submission 
            conn, addr = s.accept()
            print(f"conn from {addr}")
            tmsg = conn.recv(1024)
            #umsg = conn.recv(1024)
        
            timestamp = tmsg.decode("utf-8")
            #username = umsg.decode("utf-8")


            course = "1"
            
            time.sleep(2)
            
            API_Response = requests.get("https://tutor.dfcs-cloud.net/api/v1/getSubmissionHistory.php?apiKey=dfcs_capstone&course=" + course + "&problem=" + self.nextQ + "&start="+ timestamp, timeout = 3)

            response = API_Response.json()  #full resonse from API
            submissions = response.get("submissions")   #list of submissions
            num_submissions = response.get("size")  #number of submissions in 'submissions'


                    #check if there is more than one submission
            if num_submissions == 1:
                submission = submissions.get("0")
                    #else if more submissions check usernames ADD LATER

            print(submission)
            
            submission.pop("user_name")
            responseSeries = pd.Series(submission)
            attempt = attempt.append(responseSeries, ignore_index=True)


            if submission["score"] == "100":                
                
                
                
                attempt.graded = attempt.graded.astype(int)
                attempt.score = attempt.score.astype(int)
                qData = mb.convertRawtoClean(attempt)
                self.nextQ = mb.nextQuestion(self.nextQ, self.questionDifficulty, self.distributions, qData)
                self.questionDifficulty = self.questionDifficulty.drop([self.lastQ_index]).reset_index().drop(["index"], axis=1)

                # code to remove that question from the list of viable next questions
                self.lastQ_index = self.questionDifficulty[self.questionDifficulty['problem'] == self.nextQ].index[0]

                # set that nextQ to the problem then open that question
                path = "..\Labs\\" + self.nextQ + ".py"
                webbrowser.open(path)


                # reset attempt and submission
                attempt = pd.DataFrame(columns = columns)
                submission = ""

                
                self.QuestionLabelText = self.nextQ
                attemptNum = 1
                self.nextQSig.emit()
                print(QuestionLabelText)
                
            else:

                attemptNum = attemptNum + 1
                self.incorrect.emit()
                
    
    def stop(self):
        self.continue_run = False  # set the run condition to false on stop
        print("tutorOff")

class Gui(QWidget):

    stop_signal = pyqtSignal()  # make a stop signal to communicate with the worker in another thread
    global QuestionLabelText

    def __init__(self, nextQ, questionDifficulty, distributions):
        super(Gui, self).__init__()
        loadUi(NextQScreen, self)
        self.nextQ = nextQ
        self.questionDifficulty = questionDifficulty
        self.distributions = distributions
        self.initUI()

    def initUI(self):

        sleep(.1)
        #nextQScreen = NextQOutputScreen()
#         widget.addWidget(nextQScreen)
#         widget.setCurrentIndex(widget.currentIndex() + 1)

        self.thread = QThread()
        self.worker = Worker(self.nextQ, self.questionDifficulty, self.distributions)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.do_work)
        

#         self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
#         self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
#         self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread
        
        self.worker.nextQSig.connect(self.NextQuestion)
        self.worker.incorrect.connect(self.IncorrectUpdate)


        self.thread.start()


        self.QuestionLabel.setText(QuestionLabelText)
        self.attemptLabel.setText("Attempt Number: " + "1")


        # Thread:
        
        
        self.show()


    def startQuestion(self):
        print("ye whatevea")
    
    
    def IncorrectUpdate(self):
        self.QuestionLabel.setText("Incorrect, try again bud")
        self.attemptLabel.setText("Attempt Number: " + str(attemptNum))
        self.update
    
    def NextQuestion(self):
        
        self.QuestionLabel.setText(self.worker.QuestionLabelText)
        self.attemptLabel.setText("Attempt Number: " + str(attemptNum))
        self.update


    def skipQuestion(self):
        sleep(.25)
        



    def goBack(self):
         sleep(.25)
#         topicScreen = TopicSelectionScreen()
#         widget.addWidget(topicScreen)
#         widget.setCurrentIndex(0)


if __name__ == '__main__':
    global QuestionLabelText, nextQ, questionDifficulty, distributions
    nextQ, questionDifficulty, distributions = initialize.initialize()
    nextQ = "lsn1_helloworld"
    QuestionLabelText = nextQ
    path = "..\Labs\\" + nextQ + ".py"
    webbrowser.open(path)
    
    NextQScreen = "../View/NextQOutputScreen.ui"
    app = QApplication(sys.argv)
    gui = Gui(nextQ, questionDifficulty, distributions)
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")