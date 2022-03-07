import sys
from time import sleep

from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6 import QtWidgets

NextQScreen = "../View/NextQOutputScreen.ui"
TopicScreen = "../View/TopicSelectionScreen.ui"
TempScreen = "../View/TemporaryScreen.ui"


#Functions
class TopicSelectionScreen(QDialog):
    def __init__(self):
        super(TopicSelectionScreen, self).__init__()
        loadUi(TopicScreen, self)
        self.begin.clicked.connect(self.beginTutor)


    def beginTutor(self):
        #init userInputs
        userInput1, userInput2, userInput3, userInput4, userInput5 = 0, 0, 0, 0, 0

        #See what they pick
        if self.option1.isChecked():
             userInput1 = 1
        elif self.option2.isChecked():
             userInput2 = 1
        elif self.option3.isChecked():
             userInput3 = 1
        elif self.option4.isChecked():
             userInput4 = 1
        elif self.option5.isChecked():
             userInput5 = 1
        total = userInput1+userInput2+userInput3+userInput4+userInput5
        if  total == 0:
            self.warning.setText("Please select a topic")
        elif userInput5 == 1:
            print("Selected all topics")
        elif userInput1 == 1:
            print("Selected block 1")
        elif userInput2 == 1:
            print("Selected block 2")
        elif userInput3 == 1:
            print("Selected block 3")
        elif userInput4 == 1:
            print("Selected block 4")
        if total != 0:
            self.showTemp()

    def showTemp(self):
        sleep(.1)
        tempScreen = TemporaryScreen()
        widget.addWidget(tempScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class NextQOutputScreen(QDialog):
    def __init__(self):
        super(NextQOutputScreen, self).__init__()
        loadUi(NextQScreen, self)
        self.back.clicked.connect(self.goBack)

    def updateQuestion(self):
        sleep(.25)
        nextQScreen = NextQOutputScreen()
        widget.addWidget(nextQScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goBack(self):
        sleep(.25)
        topicScreen = TopicSelectionScreen()
        widget.addWidget(topicScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def showTemp(self):
        sleep(.25)
        tempScreen = TemporaryScreen()
        widget.addWidget(tempScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class TemporaryScreen(QDialog):
    def __init__(self):
        super(TemporaryScreen, self).__init__()
        loadUi(TempScreen, self)
        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        sleep(.25)
        TopicScreen = TopicSelectionScreen()
        widget.addWidget(TopicScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

# Main
app = QApplication(sys.argv)
TopicSelection = TopicSelectionScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(TopicSelection)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")
