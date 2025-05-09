from tkinter import *
from logic import *

class Gui:
	def __init__(self, window):
		#window
		self.window = window

#frame for course, entry
		self.frame_course = Frame(self.window)
		self.label_course = Label(self.frame_course, text='Course:')
		self.input_course = Entry(self.frame_course, width=20)
		self.label_course.pack(side='left', pady=10, padx=38)
		self.input_course.pack(side='left')
		self.frame_course.pack(anchor='w')

#frame for no of assessments, entry
		self.frame_num = Frame(self.window)
		self.label_num_assess = Label(self.frame_num, text='No. of Assessments:')
		self.input_num_assess = Entry(self.frame_num, width=20)
		#generate button
		self.button_num_assess = Button(self.frame_num, text='generate?', command=lambda: self.generate())
		self.label_num_assess.pack(side='left', pady=10, padx=5)
		self.input_num_assess.pack(side='left')
		self.button_num_assess.pack(side='left', padx=5)
		self.frame_num.pack(anchor='w')

#frame for assessment 1
		self.frame_assess1 = Frame(self.window)
		self.label_assess1 = Label(self.frame_assess1, text='Assessment 1')
		self.input_assess1_score = Entry(self.frame_assess1, width=10)
		self.input_assess1_weight = Entry(self.frame_assess1, width=10)
		self.label_assess1.pack(side='left', pady=10, padx=5)
		self.input_assess1_score.pack(side='left', padx=5)
		self.input_assess1_weight.pack(side='left', padx=5)

#frame for assessment 2
		self.frame_assess2 = Frame(self.window)
		self.label_assess2 = Label(self.frame_assess2, text='Assessment 2')
		self.input_assess2_score = Entry(self.frame_assess2, width=10)
		self.input_assess2_weight = Entry(self.frame_assess2, width=10)
		self.label_assess2.pack(side='left', pady=10, padx=5)
		self.input_assess2_score.pack(side='left', padx=5)
		self.input_assess2_weight.pack(side='left', padx=5)

#frame for assessment 3
		self.frame_assess3 = Frame(self.window)
		self.label_assess3 = Label(self.frame_assess3, text='Assessment 3')
		self.input_assess3_score = Entry(self.frame_assess3, width=10)
		self.input_assess3_weight = Entry(self.frame_assess3, width=10)
		self.label_assess3.pack(side='left', pady=10, padx=5)
		self.input_assess3_score.pack(side='left', padx=5)
		self.input_assess3_weight.pack(side='left', padx=5)

#frame for assessment 4
		self.frame_assess4 = Frame(self.window)
		self.label_assess4 = Label(self.frame_assess4, text='Assessment 4')
		self.input_assess4_score = Entry(self.frame_assess4, width=10)
		self.input_assess4_weight = Entry(self.frame_assess4, width=10)
		self.label_assess4.pack(side='left', pady=10, padx=5)
		self.input_assess4_score.pack(side='left', padx=5)
		self.input_assess4_weight.pack(side='left', padx=5)

#frame for assessment 5
		self.frame_assess5 = Frame(self.window)
		self.label_assess5 = Label(self.frame_assess5, text='Assessment 5')
		self.input_assess5_score = Entry(self.frame_assess5, width=10)
		self.input_assess5_weight = Entry(self.frame_assess5, width=10)
		self.label_assess5.pack(side='left', pady=10, padx=5)
		self.input_assess5_score.pack(side='left', padx=5)
		self.input_assess5_weight.pack(side='left', padx=5)

		# label for notices
		self.label_notice = Label(self.window, text='')
		self.button_submit = Button(self.window, text='SUBMIT')
		# submit button
		self.button_submit.pack(side='bottom', pady=10)
		self.label_notice.pack(side='bottom', pady=10)


	def generate(self):
		try:
			num_assess = int(self.input_num_assess.get())
			self.label_notice.config(text='')

			if num_assess == 1:
				self.frame_assess1.pack()
				self.frame_assess2.pack_forget()
				self.frame_assess3.pack_forget()
				self.frame_assess4.pack_forget()
				self.frame_assess5.pack_forget()
			elif num_assess == 2:
				self.frame_assess1.pack()
				self.frame_assess2.pack()
				self.frame_assess3.pack_forget()
				self.frame_assess4.pack_forget()
				self.frame_assess5.pack_forget()
			elif num_assess == 3:
				self.frame_assess1.pack()
				self.frame_assess2.pack()
				self.frame_assess3.pack()
				self.frame_assess4.pack_forget()
				self.frame_assess5.pack_forget()
			elif num_assess == 4:
				self.frame_assess1.pack()
				self.frame_assess2.pack()
				self.frame_assess3.pack()
				self.frame_assess4.pack()
				self.frame_assess5.pack_forget()
			elif num_assess == 5:
				self.frame_assess1.pack()
				self.frame_assess2.pack()
				self.frame_assess3.pack()
				self.frame_assess4.pack()
				self.frame_assess5.pack()
			else:
				self.label_notice.config(text='Enter value [1-5]')
		except ValueError:
			self.label_notice.config(text='Enter value [1-5]')




