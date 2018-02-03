#!/Users/huseyinkandir/anaconda3/bin/python

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QSizePolicy, QLabel, QDialog)
from PyQt5 import QtGui

import json
import pprint as pp

class Example(QWidget):
    Questions = {}

    def __init__(self):
        super().__init__()

        self.initUI()
#        self.dialog = Second(self)

    def on_pushButton10_clicked(self):
        global Questions
        d = QDialog()
        d.setWindowTitle("Question")
#        d.setWindowModality(Qt.ApplicationModal)
        gridChild = QGridLayout()
        d.setLayout(gridChild)
        newfont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)

        positions = [(i,j) for i in range(4) for j in range(1)]

        lable = QLabel("question")
        lable.setFont(newfont)
        gridChild.addWidget(lable, *positions[0])
        lable = QLabel(Questions['Vocabulary']['0']['question'])
        lable.setFont(newfont)
        gridChild.addWidget(lable, *positions[1])

        d.exec_()

    def on_pushButton11_clicked(self):
        d = QDialog()
        d.setWindowTitle("Question")
#        d.setWindowModality(Qt.ApplicationModal)
        gridChild = QGridLayout()
        d.setLayout(gridChild)
        newfont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)

        positions = [(i,j) for i in range(4) for j in range(1)]

        lable = QLabel("name2")
        lable.setFont(newfont)
#               button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        gridChild.addWidget(lable, *positions[0])

        d.exec_()


    def initUI(self):
        global Questions
        # Reading Questions
        with open('Questions.json', 'r') as f:
             Questions = json.load(f)

        grid = QGridLayout()
        self.setLayout(grid)

        question_names = ['QUESTION', '', '', '',
                 'What is .....?', '', '', '',
                'Timer', '', '', '',
                 'Group 1 +', 'Group 2 +', '', '',
                '', '', '', '',
                '', '', '', '']

        names = ['Vocabulary', 'Grammer', 'Tenses', 'Punctuation',
                 '10', '10', '10', '10',
                '20', '20', '20', '20',
                 '30', '30', '30', '30',
                '40', '40', '40', '40',
                'Timer:', 'Score Group1:', 'Score Group2:', '']
        newfont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)

        positions = [(i,j) for i in range(6) for j in range(4)]

        lable00 = QLabel(names[0])
        lable00.setFont(newfont)
        grid.addWidget(lable00, *positions[0])
        lable01 = QLabel(names[1])
        lable01.setFont(newfont)
        grid.addWidget(lable01, *positions[1])
        lable02 = QLabel(names[2])
        lable02.setFont(newfont)
        grid.addWidget(lable02, *positions[2])
        lable03 = QLabel(names[3])
        lable03.setFont(newfont)
        grid.addWidget(lable03, *positions[3])

        button10 = QPushButton('bla1')
        button10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button10.clicked.connect(self.on_pushButton10_clicked)
        grid.addWidget(button10, *positions[4])
        button11 = QPushButton('bla2')
        button11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button11.clicked.connect(self.on_pushButton11_clicked)
        grid.addWidget(button11, *positions[5])
        button12 = QPushButton('bla')
        button12.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button12.clicked.connect(lambda: self.on_pushButton12_clicked())
        grid.addWidget(button12, *positions[6])
        button13 = QPushButton('bla')
        button13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button13.clicked.connect(lambda: self.on_pushButton13_clicked())
        grid.addWidget(button13, *positions[7])
        button20 = QPushButton('bla')
        button20.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button20.clicked.connect(lambda: self.on_pushButton20_clicked())
        grid.addWidget(button20, *positions[8])
        button21 = QPushButton('bla')
        button21.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button21.clicked.connect(lambda: self.on_pushButton21_clicked())
        grid.addWidget(button21, *positions[9])
        button22 = QPushButton('bla')
        button22.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button22.clicked.connect(lambda: self.on_pushButton22_clicked())
        grid.addWidget(button22, *positions[10])
        button23 = QPushButton('bla')
        button23.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button23.clicked.connect(lambda: self.on_pushButton23_clicked())
        grid.addWidget(button23, *positions[11])
        button30 = QPushButton('bla')
        button30.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button30.clicked.connect(lambda: self.on_pushButton30_clicked())
        grid.addWidget(button30, *positions[12])
        button31 = QPushButton('bla')
        button31.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button31.clicked.connect(lambda: self.on_pushButton31_clicked())
        grid.addWidget(button31, *positions[13])
        button32 = QPushButton('bla')
        button32.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button32.clicked.connect(lambda: self.on_pushButton32_clicked())
        grid.addWidget(button32, *positions[14])
        button33 = QPushButton('bla')
        button33.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button33.clicked.connect(lambda: self.on_pushButton33_clicked())
        grid.addWidget(button33, *positions[15])
        button40 = QPushButton('bla')
        button40.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button40.clicked.connect(lambda: self.on_pushButton40_clicked())
        grid.addWidget(button40, *positions[16])
        button41 = QPushButton('bla')
        button41.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button41.clicked.connect(lambda: self.on_pushButton41_clicked())
        grid.addWidget(button41, *positions[17])
        button42 = QPushButton('bla')
        button42.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button42.clicked.connect(lambda: self.on_pushButton42_clicked())
        grid.addWidget(button42, *positions[18])
        button43 = QPushButton('bla')
        button43.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        button43.clicked.connect(lambda: self.on_pushButton43_clicked())
        grid.addWidget(button43, *positions[19])




#         for position, name in zip(positions, names):
#             data = str(position[0])+str(position[1])
#             print(*position)
#             if True == name.isnumeric():
#                 button = QPushButton(name)
#                 button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
#                 button.clicked.connect(lambda: self.on_pushButton_clicked(question_names))
#                 grid.addWidget(button, *position)
#             elif False == name.isnumeric():
#                 lable = QLabel(name)
#                 lable.setFont(newfont)
# #               button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
#                 grid.addWidget(lable, *position)
#             else:
#                 pass

        self.move(300, 300)
        self.setWindowTitle('Game')
        self.show()


if __name__ == '__main__':

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
