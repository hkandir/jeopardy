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

    def on_pushButton_clicked(self, names):
        print("button:names", names)
        d = QDialog()
#        b1 = QPushButton("ok",d)
#        b1.move(50,50)
        d.setWindowTitle("Question")
#        d.setWindowModality(Qt.ApplicationModal)

        gridChild = QGridLayout()
        d.setLayout(gridChild)


        newfont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)

        positions = [(i,j) for i in range(4) for j in range(1)]

        for position, name in zip(positions, names):
            # lable = QLabel(names[name])
            # lable.setFont(newfont)
            # button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
            # gridChild.addWidget(lable, *position)

            print("on_pushButton_clicked:position, name", position, type(name))
            lable = QLabel(str(name))
            lable.setFont(newfont)
#               button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
            gridChild.addWidget(lable, *position)


        d.exec_()

    def GetQuestions(self, questionGroup, questionNumber):
        global Questions
        quests = Questions[questionGroup][questionNumber]
        ret = []
        for q in quests:
            ret.append(quests[q])
        return ret

    def initUI(self):
        global Questions
        # Reading Questions
        with open('Questions.json', 'r') as f:
             Questions = json.load(f)

        grid = QGridLayout()
        self.setLayout(grid)


        question_names =    [[""],[""],[""],[""]],[[""],[""],[""],[""]],\
                            [[""],[""],[""],[""]],[[""],[""],[""],[""]]
        names = ['Vocabulary', 'Grammer', 'Tenses', 'Punctuation',
                 '10', '10', '10', '10',
                '20', '20', '20', '20',
                 '30', '30', '30', '30',
                '40', '40', '40', '40',
                'Timer:', 'Score EURA:', 'Score HUS:', '']
        questionGroups = ['Vocabulary', 'Grammer', 'Tenses', 'Punctuation']
        questionNumbers = ['0', '1', '2', '3']
        # questionDetails = ['question', 'timer', 'nameGroup1', 'nameGroup2']

        newfont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)

        positions = [(i,j) for i in range(7) for j in range(4)]
        print(positions)
        print(*positions)
        # print("zipStart")
        # list(zip(positions, names, questionGroups, questionNumbers))
        # print("zipEnd")
        for position, name in zip(positions, names):
            # data = str(position[0])+str(position[1])
            # print(data)
            print("position,name:", position, name)

            if True == name.isnumeric():
                button = QPushButton(name)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                for title in Questions[names[position[0]-1]][questionNumbers[position[1]]]:
                    question_names[position[0]-1][position[1]] = self.GetQuestions(names[position[0]-1],questionNumbers[position[1]])
                # print(question_names)
                    # print(Questions[questionGroups[position[1]]])
                # print("position[0]-1, position[1]", position[0]-1, position[1])
                # print(Questions[questionGroups[position[0]-1]][questionNumbers[position[1]]])
                # print(self.GetQuestions(names[position[0]-1], questionNumbers[position[1]], 'question'))
                # question_names[4]= self.GetQuestions(names[position[0]-1], questionNumbers[position[1]], 'question')
                # button.clicked.connect(lambda: self.on_pushButton_clicked(Questions[questionGroups[position[0]-1]][questionNumbers[position[1]]]))
                print(position[0]-1, position[1])
                print(question_names[position[0]-1][position[1]])
                button.clicked.connect(lambda state, x=question_names[position[0]-1][position[1]]: self.on_pushButton_clicked(x))
                # icon = QtGui.QIcon()
                # icon.addPixmap(QtGui.QPixmap("GreenSquareButton.png"))
                # # button.setFlat(True)
                # # button.setAutoFillBackground(True)
                # button.setIcon(icon)
                # button.setStyleSheet("background-image: url(GreenSquareButton.png); background-attachment: fixed")
                button.setStyleSheet("border-image: url(GreenSquareButton.png)")
                button.setFont(QtGui.QFont("Times", 40, QtGui.QFont.Bold))
                grid.addWidget(button, *position)
            elif False == name.isnumeric():
                lable = QLabel(name)
                lable.setFont(newfont)
#               button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
                grid.addWidget(lable, *position)
            else:
                pass

        pp.pprint(question_names)
        self.move(300, 300)
        self.setWindowTitle('Game')
        self.show()


if __name__ == '__main__':

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
