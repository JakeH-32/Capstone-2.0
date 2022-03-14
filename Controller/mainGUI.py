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
import dummyMain

NextQScreen = "NextQOutputScreen.ui"
TopicScreen = "TopicSelectionScreen.ui"
QuestionLabelText = "Problem #1"
LinkToCanvas="<a href=\"https://canvas.instructure.com/courses/4116250\">'Click here to go to Canvas Page'</a>"



class Lthread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # helper function to execute the threads
    def run(self):
        L = listner()
        


class listner():
    
    def __init__(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        host = socket.gethostname()
        port = 5555
        
        try:
            s.bind((host, port))
        except socket.error as s:
            print(str(es))
        
        s.listen(1)   

        columns = ["student_id", "problem","timestamp","graded","score","sourcehash"]
        attempt = pd.DataFrame(columns = columns)
        nextQ, questionDifficulty, distributions = dummyMain.initialize()
        
        i = 1
        while (True):
            print("waiting")
            # waits for notification from autograder, then fetches new submission 
            conn, addr = s.accept()
            print(f"conn from {addr}")
            tmsg = conn.recv(1024)
            #umsg = conn.recv(1024)
        
            timestamp = tmsg.decode("utf-8")
            #username = umsg.decode("utf-8")


            problem = "sample"
            course = "1"
            
            time.sleep(.5)
            
            API_Response = requests.get("https://tutor.dfcs-cloud.net/api/v1/getSubmissionHistory.php?apiKey=dfcs_capstone&course=" + course + "&problem=" + problem + "&start="+ timestamp, timeout = 3)

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
                # change the column type of the attempt data
                attempt.graded = attempt.graded.astype(int)
                attempt.score = attempt.score.astype(int)
                
                # condense to one dataframe row
                qData = mb.convertRawtoClean(attempt)
                
                # if its the first time going to the next Q, give it the "a4" question
                if i == 1:
                    nextQ = mb.nextQuestion("a4_1_lift", questionDifficulty, distributions, qData)
                else:  # in all other cases, use the "problem"
                    nextQ = mb.nextQuestion(problem, questionDifficulty, distributions, qData)
                
                i += 1
                
                # code to remove that question from the list of viable next questions
                lastQ_index = questionDifficulty[questionDifficulty['problem'] == problem].index[0]
                questionDifficulty = questionDifficulty.drop([lastQ_index]).reset_index().drop(["Unnamed: 0"], axis=1).drop(["index"], axis=1)
                
                # set that nextQ to the problem
                problem = nextQ
                
                # reset attempt and submission
                attempt = pd.DataFrame(columns = columns)
                submission = ""
                
                # throw that shit into the GUI right here. We can add an exit to the while loop as long as you call this function again afterwards
                QuestionLabelText = nextQ
                print(QuestionLabelText)


# Screen Classes
class TopicSelectionScreen(QDialog):
    def __init__(self):
        super(TopicSelectionScreen, self).__init__()
        loadUi(TopicScreen, self)
        self.begin.clicked.connect(self.beginTutor)
        
        

    def beginTutor(self):
        # init userInputs
        userInput1, userInput2, userInput3, userInput4, userInput5 = 0, 0, 0, 0, 0

        # See what they pick
        if self.option1.isChecked():
            userInput1 = 1
        if self.option2.isChecked():
            userInput2 = 1
        if self.option3.isChecked():
            userInput3 = 1
        if self.option4.isChecked():
            userInput4 = 1
        if self.option5.isChecked():
            userInput5 = 1

        total = userInput1 + userInput2 + userInput3 + userInput4 + userInput5
        if total == 0:
            self.warning.setText("Please select a topic")
        elif userInput5 == 1:
            print("Selected all topics")
        if userInput1 == 1:
            print("Selected block 1")
        if userInput2 == 1:
            print("Selected block 2")
        if userInput3 == 1:
            print("Selected block 3")
        if userInput4 == 1:
            print("Selected block 4")
        if total != 0:
            self.showQuestion()

    def showQuestion(self):
        sleep(.1)
        nextQScreen = NextQOutputScreen()
        widget.addWidget(nextQScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class NextQOutputScreen(QDialog):
    def __init__(self):
        super(NextQOutputScreen, self).__init__()
        loadUi(NextQScreen, self)
        
        self.threadpool = QThreadPool()
        
        self.backButton.clicked.connect(self.goBack)
        self.QuestionLabel.setText(QuestionLabelText)

        self.startButton.clicked.connect(self.startQuestion)
        self.label.setText(LinkToCanvas)
        self.skipButton.clicked.connect(self.skipQuestion)


    def startQuestion(self):
        worker = Worker(self.listner)
        
        # Add listener here
        # for i in range(10):
        # self.startButton.setEnabled(False)
        
        self.threadpool.start(worker)

        #Run code before here


    def skipQuestion(self):
        sleep(.25)
        nextQScreen = NextQOutputScreen()
        widget.addWidget(nextQScreen)
        widget.setCurrentIndex(widget.currentIndex())
        self.QuestionLabel.setText("Question Skipped")



    def goBack(self):
        sleep(.25)
        topicScreen = TopicSelectionScreen()
        widget.addWidget(topicScreen)
        widget.setCurrentIndex(0)




class Qthread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # helper function to execute the threads
    def run(self):
        global widget
        app = QApplication(sys.argv)
        TopicSelection = TopicSelectionScreen()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(TopicSelection)
        widget.show()

        try:
            sys.exit(app.exec())
        except:
            print("Exiting")
# Main



threadListner = Lthread("Listner", 1000)
threadGUI = Qthread("GUI", 2000)

threadListner.start()
threadGUI.start()

# 

