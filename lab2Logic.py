from PyQt6.QtWidgets import QMainWindow
from lab2Gui import *

class Lab2Logic(QMainWindow, Ui_mainWindow):
    '''
    class to handle Lab 2 (Grading) logic
    '''
    def __init__(self):
        '''
        function to initialize Lab2Logic class
        '''
        super().__init__()
        self.setupUi(self)
        self.numStudents = 0
        self.alreadyPressed = False
        self.scores = []

        self.pushButton_Store.clicked.connect(self.store)
        self.pushButton_Calculate.clicked.connect(self.calculate)
        self.pushButton_Clear.clicked.connect(self.clear)

    def store(self):
        '''
        function for the store button on the Gui, takes in value of number of students and adjusts accordingly
        '''
        self.numStudents = int(self.textEdit_num.toPlainText())
        self.label_num_2.setText(f'Enter {self.numStudents} scores (1 space)')
        self.alreadyPressed = True

    def calculate(self):
        '''
        function for the Calculate! button on the Gui, takes in individual student scores, assigns them to a list, and calculates grades and average score
        '''
        if self.alreadyPressed:
            try:
                self.label_Error.setText('')
                self.scoreStr = str(self.textEdit_num_2.toPlainText())
                self.scores = self.scoreStr.split()

                if len(self.scores) < self.numStudents:
                    while len(self.scores) < self.numStudents:
                        self.label_Error.setText('Input correct # of scores')
                        break
                if len(self.scores) > self.numStudents:
                    self.scores = self.scores[:self.numStudents]

                max_score = float('-inf')
                average = 0
                for score in self.scores:
                    score = int(score)
                    average += score
                    if score > max_score:
                        max_score = score
                average /= len(self.scores)

                studNum = 1
                labelNum = 0  # Initialize labelNum here
                for score in self.scores:
                    score = int(score)
                    self.listWidget_Scores.item(labelNum).setText(
                        f'Student {studNum} score is {score} and grade is {self.letterGrade(max_score, score)}'
                    )
                    studNum += 1
                    labelNum += 1  # Increment labelNum to move to the next item
                self.listWidget_Scores.item(10).setText(
                    f'The average score is {average}, a score of {self.letterGrade(max_score, average)}'
                )
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            self.label_Error.setText('Need to Store Number of Students!')


    def clear(self):
        '''
        function clears all the input and dialog boxes
        '''
        self.textEdit_num.clear()
        self.textEdit_num_2.clear()
        self.label_num_2.clear()
        self.label_Error.clear()
        self.listWidget_Scores.clear()


    def letterGrade(self,max_score: int, kid_score: int):
        '''
        Function responsible for determining the letter grade of each student
        :param max_score: The largers score in scores
        :param kid_score: The score that the grade is getting assigned to
        :return: the letter grade recieved
        '''
        grade = 'F'
        if (kid_score >= max_score - 40):
            grade = 'D'
        if (kid_score >= max_score - 30):
            grade = 'C'
        if (kid_score >= max_score - 20):
            grade = 'B'
        if (kid_score >= max_score - 10):
            grade = 'A'
        return grade

