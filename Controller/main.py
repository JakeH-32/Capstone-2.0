import sys
import time
from time import sleep
import dummyMain
import time
import pandas as pd
import socket
import numpy as np
import datetime
import matplotlib.pyplot as plt
import modelBuilder as mb
import main
import sys
import requests
import json

from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6 import QtWidgets

NextQScreen = "../View/NextQOutputScreen.ui"
TopicScreen = "../View/TopicSelectionScreen.ui"
QuestionLabelText = "Problem #1"
LinkToCanvas="<a href=\"https://canvas.instructure.com/courses/4116250\">'Click here to go to Canvas Page'</a>"


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
        self.backButton.clicked.connect(self.goBack)
        self.skipButton.clicked.connect(self.skipQuestion)
        self.QuestionLabel.setText(QuestionLabelText)
        
        self.startButton.clicked.connect(self.startQuestion)
        self.label.setText(LinkToCanvas)


        # while not self.skipButton.clicked.connect(self.skipQuestion()):
        #     print("Sleeping")

    def startQuestion(self):
        host = socket.gethostname()
        port = 5555
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.bind((host, port))
        except socket.error as es:
            print(str(es))
        
        s.listen(5)
        
        nextQ, questionDifficulty, distributions = dummyMain.initialize()
        columns = ["student_id", "problem", "timestamp", "graded", "score", "sourcehash"]
        attempt = pd.DataFrame(columns=columns)
        submission = {}
        submission["score"] = 0
        while submission["score"] != 100.0:
            # waits for notification from autograder, then fetches new submission
            conn, addr = s.accept()
            print(f"conn from {addr}")
            tmsg = conn.recv(1024)
            # umsg = conn.recv(1024)

            timestamp = tmsg.decode("utf-8")
            # username = umsg.decode("utf-8")

            problem = "sample"
            # problem = nextQ
            course = "1"

            API_Response = requests.get(
                "https://tutor.dfcs-cloud.net/api/v1/getSubmissionHistory.php?apiKey=dfcs_capstone&course=" + course + "&problem=" + problem + "&start=" + timestamp,
                timeout=3)

            response = API_Response.json()  # full resonse from API
            submissions = response.get("submissions")  # list of submissions
            num_submissions = response.get("size")  # number of submissions in 'submissions'

            # check if there is more than one submission
            if num_submissions == 1:
                submission = submissions.get("0")
            # else if more submissions check usernames ADD LATER

            submission.pop("user_name")
            responseSeries = pd.Series(submission)
            attempt = attempt.append(responseSeries, ignore_index=True)

        qData = mb.convertRawtoClean(attempt)
        nextQ = mb.nextQuestion(problem, questionDifficulty, distributions, qData)
        attempt = pd.DataFrame(columns=columns)
        submission = ""
        QuestionLabelText = nextQ

        nextQScreen = NextQOutputScreen()
        widget.addWidget(nextQScreen)
        widget.setCurrentIndex(widget.currentIndex())
        self.QuestionLabel.setText(nextQ)

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
        widget.setCurrentIndex(widget.currentIndex() + 1)



# Main
global host, port, s, columns, attempt, nextQ, questionDifficulty, distributions

nextQ, questionDifficulty, distributions = dummyMain.initialize()

app = QApplication(sys.argv)
TopicSelection = TopicSelectionScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(TopicSelection)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")
