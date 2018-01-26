

"""
ZetCode PyQt5 tutorial

In this example, we create a skeleton
of a calculator using QGridLayout.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication, QSizePolicy, QLabel, QDialog)
from PyQt5 import QtGui



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
#        self.dialog = Second(self)

    def on_pushButton_clicked(self, names):
        d = QDialog()
#        b1 = QPushButton("ok",d)
#        b1.move(50,50)
        d.setWindowTitle("Question")
#        d.setWindowModality(Qt.ApplicationModal)

        gridChild = QGridLayout()
        d.setLayout(gridChild)

        # names = ['QUESTION', '', '', '',
        #          'What is .....?', '', '', '',
        #         'Timer', '', '', '',
        #          'Group 1 +', 'Group 2 +', '', '',
        #         '', '', '', '',
        #         '', '', '', '']
        newfont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)

        positions = [(i,j) for i in range(6) for j in range(4)]

        for position, name in zip(positions, names):

            if True == name.isnumeric():
                button = QPushButton(name)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
                button.clicked.connect(d.on_pushButton_clicked)
                gridChild.addWidget(button, *position)
            elif False == name.isnumeric():
                lable = QLabel(name)
                lable.setFont(newfont)
#               button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
                gridChild.addWidget(lable, *position)
            else:
                pass

        d.exec_()


    def initUI(self):

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

        for position, name in zip(positions, names):
            data = str(position[0])+str(position[1])
            print(data)
            if True == name.isnumeric():
                button = QPushButton(name)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
                button.clicked.connect(lambda: self.on_pushButton_clicked(question_names))
                grid.addWidget(button, *position)
            elif False == name.isnumeric():
                lable = QLabel(name)
                lable.setFont(newfont)
#               button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
                grid.addWidget(lable, *position)
            else:
                pass

        self.move(300, 300)
        self.setWindowTitle('Game')
        self.show()


if __name__ == '__main__':

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
