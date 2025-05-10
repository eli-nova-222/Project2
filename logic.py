from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#hide all assess fields on setup
        self.label_assess1.hide()
        self.input_assess1.hide()

        self.label_assess2.hide()
        self.input_assess2.hide()

        self.label_assess3.hide()
        self.input_assess3.hide()

        self.label_assess4.hide()
        self.input_assess4.hide()

        self.label_assess5.hide()
        self.input_assess5.hide()

#hide results labels and submit button
        #avg score/letter
        self.label_avg_score.hide()
        self.score_label.hide()

        self.label_avg_letter.hide()
        self.letter_label.hide()

        self.button_submit.hide()
        #set notice text blank
        self.label_notice.setText('')








        self.button_generate.clicked.connect(lambda: self.generate())

    def generate(self):
        try:
            num_assess = int(self.input_num_assess.text().strip())



        except ValueError:
            self.label_notice.setText(f'Must choose digit in range [1-5]')
            self.input_num_assess.setText('')
