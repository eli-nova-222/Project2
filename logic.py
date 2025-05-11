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

        #generate button action
        self.button_generate.clicked.connect(lambda: self.generate())
        #submit button action
        self.button_submit.clicked.connect(lambda : self.submit())

    #function for generate button
    def generate(self):
        try:
            course_name = str(self.input_course.text().strip())
            num_assess = int(self.input_num_assess.text().strip())
            self.label_notice.setText('')
            if course_name == '':
                raise UserWarning

            if num_assess == 1:
                self.label_assess1.show()
                self.input_assess1.show()
                self.label_assess2.hide()
                self.input_assess2.hide()
                self.label_assess3.hide()
                self.input_assess3.hide()
                self.label_assess4.hide()
                self.input_assess4.hide()
                self.label_assess5.hide()
                self.input_assess5.hide()
                self.button_submit.show()
                return 1
            elif num_assess == 2:
                self.label_assess1.show()
                self.input_assess1.show()
                self.label_assess2.show()
                self.input_assess2.show()
                self.label_assess3.hide()
                self.input_assess3.hide()
                self.label_assess4.hide()
                self.input_assess4.hide()
                self.label_assess5.hide()
                self.input_assess5.hide()
                self.button_submit.show()
                return 2
            elif num_assess == 3:
                self.label_assess1.show()
                self.input_assess1.show()
                self.label_assess2.show()
                self.input_assess2.show()
                self.label_assess3.show()
                self.input_assess3.show()
                self.label_assess4.hide()
                self.input_assess4.hide()
                self.label_assess5.hide()
                self.input_assess5.hide()
                self.button_submit.show()
                return 3
            elif num_assess == 4:
                self.label_assess1.show()
                self.input_assess1.show()
                self.label_assess2.show()
                self.input_assess2.show()
                self.label_assess3.show()
                self.input_assess3.show()
                self.label_assess4.show()
                self.input_assess4.show()
                self.label_assess5.hide()
                self.input_assess5.hide()
                self.button_submit.show()
                return 4
            elif num_assess == 5:
                self.label_assess1.show()
                self.input_assess1.show()
                self.label_assess2.show()
                self.input_assess2.show()
                self.label_assess3.show()
                self.input_assess3.show()
                self.label_assess4.show()
                self.input_assess4.show()
                self.label_assess5.show()
                self.input_assess5.show()
                self.button_submit.show()
                return 5
            else:
                raise ValueError

        except ValueError:
            self.label_notice.setText(f'Must choose digit in range [1-5]')
            self.input_num_assess.setText('')
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
            self.button_submit.hide()
        except UserWarning:
            self.label_notice.setText(f'Must enter course identifier')

    #function for submit button
    def submit(self):
        assess_val = self.generate()
        self.label_avg_score.show()
        self.label_avg_letter.show()

        try:
            if assess_val == 1:
                summed_scores = int(self.input_assess1.text())
                average_scores = summed_scores/1
                self.score_label.setText(f'{average_scores:.2f}')
                self.score_label.show()
                self.letter_score(average_scores)
            elif assess_val == 2:
                summed_scores = int(self.input_assess1.text()) + int(self.input_assess2.text())
                average_scores = summed_scores / 2
                self.score_label.setText(f'{average_scores:.2f}')
                self.score_label.show()
                self.letter_score(average_scores)
            elif assess_val == 3:
                summed_scores = (int(self.input_assess1.text()) + int(self.input_assess2.text())
                                 + int(self.input_assess3.text()))
                average_scores = summed_scores / 3
                self.score_label.setText(f'{average_scores:.2f}')
                self.score_label.show()
                self.letter_score(average_scores)
            elif assess_val == 4:
                summed_scores = (int(self.input_assess1.text()) + int(self.input_assess2.text())
                                 + int(self.input_assess3.text()) + int(self.input_assess4.text()))
                average_scores = summed_scores / 4
                self.score_label.setText(f'{average_scores:.2f}')
                self.score_label.show()
                self.letter_score(average_scores)
            elif assess_val == 5:
                summed_scores = (int(self.input_assess1.text()) + int(self.input_assess2.text())
                                 + int(self.input_assess3.text()) + int(self.input_assess4.text())
                                 + int(self.input_assess5.text()))
                average_scores = summed_scores / 5
                self.score_label.setText(f'{average_scores:.2f}')
                self.score_label.show()
                self.letter_score(average_scores)

        except ValueError:
            self.label_notice.setText(f'Please enter numerical scores')

        else:
            self.write_file()

    #function for letter score
    def letter_score(self,grade_var):
        letter_val = grade_var
        if letter_val >= 90:
            letter_grade = "A"
            self.letter_label.setText(letter_grade)
            self.letter_label.show()
        elif letter_val >= 80:
            letter_grade = "B"
            self.letter_label.setText(letter_grade)
            self.letter_label.show()
        elif letter_val >= 70:
            letter_grade = "C"
            self.letter_label.setText(letter_grade)
            self.letter_label.show()
        elif letter_val >= 60:
            letter_grade = "D"
            self.letter_label.setText(letter_grade)
            self.letter_label.show()
        elif letter_val <= 59:
            letter_grade = "F"
            self.letter_label.setText(letter_grade)
            self.letter_label.show()

    #function to write to csv file
    def write_file(self):
        assess_val = self.generate()
        course_id = self.input_course.text()
        test1 = 0
        test2 = 0
        test3 = 0
        test4 = 0
        test5 = 0

        if assess_val == 1:
            test1 = self.input_assess1.text()
        elif assess_val == 2:
            test1 = self.input_assess1.text()
            test2 = self.input_assess2.text()
        elif assess_val == 3:
            test1 = self.input_assess1.text()
            test2 = self.input_assess2.text()
            test3 = self.input_assess3.text()
        elif assess_val == 4:
            test1 = self.input_assess1.text()
            test2 = self.input_assess2.text()
            test3 = self.input_assess3.text()
            test4 = self.input_assess4.text()
        elif assess_val == 5:
            test1 = self.input_assess1.text()
            test2 = self.input_assess2.text()
            test3 = self.input_assess3.text()
            test4 = self.input_assess4.text()
            test5 = self.input_assess5.text()


        with open('grades.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            grade_data = [course_id, test1, test2, test3, test4, test5]
            writer.writerow(grade_data)
