from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys, glob, os
import cv2, imutils

BUFFER_SIZE = 5

class AppWindow(QMainWindow):
	def __init__(self, image_list):
		super(AppWindow, self).__init__()
		self.image_list = image_list
		self.number_of_images = len(self.image_list)
		self.curr_image_index = 0
		self.display_image = self.image_list[self.curr_image_index]

		self.buffer_start = self.curr_image_index
		self.buffer_end = self.curr_image_index + BUFFER_SIZE

		self.initUI()

	def updatePhoto(self):
	    self.display_image = self.image_list[self.curr_image_index]

	def nextPhoto(self):
		if self.curr_image_index < self.number_of_images-1:
			self.curr_image_index += 1
			self.updatePhoto()
			self.setPhoto()

		if self.curr_image_index == self.buffer_end:
			self.buffer_end += 1
			self.buffer_start += 1
			self.setBuffer()

	def previousPhoto(self):
		if self.curr_image_index > 0:
			self.curr_image_index -= 1
			self.updatePhoto()
			self.setPhoto()

		if self.curr_image_index == self.buffer_start-1:
			self.buffer_end -= 1
			self.buffer_start -= 1
			self.setBuffer()

	def setPhoto(self):
		image = self.display_image
		image = imutils.resize(image, height=600) if image.shape[0] > image.shape[1] else imutils.resize(image, width=600)
		frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
		self.canvas.setPixmap(QtGui.QPixmap.fromImage(image))
		self.canvas.setAlignment(QtCore.Qt.AlignCenter)

	def setBuffer(self):
		images = []
		range_of_mini_display = min(BUFFER_SIZE, self.number_of_images)

		for index in range(range_of_mini_display):
			image = self.image_list[self.buffer_start + index]
			image = imutils.resize(image, height=120) if image.shape[0] > image.shape[1] else imutils.resize(image, width=120)
			frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
			images.append(image)

		if range_of_mini_display > 0:
			self.canvasBuffer_0.setPixmap(QtGui.QPixmap.fromImage(images[0]))
			self.canvasBuffer_0.setAlignment(QtCore.Qt.AlignCenter)
		if range_of_mini_display > 1:
			self.canvasBuffer_1.setPixmap(QtGui.QPixmap.fromImage(images[1]))
			self.canvasBuffer_1.setAlignment(QtCore.Qt.AlignCenter)
		if range_of_mini_display > 2:
			self.canvasBuffer_2.setPixmap(QtGui.QPixmap.fromImage(images[2]))
			self.canvasBuffer_2.setAlignment(QtCore.Qt.AlignCenter)
		if range_of_mini_display > 3:
			self.canvasBuffer_3.setPixmap(QtGui.QPixmap.fromImage(images[3]))
			self.canvasBuffer_3.setAlignment(QtCore.Qt.AlignCenter)
		if range_of_mini_display > 4:
			self.canvasBuffer_4.setPixmap(QtGui.QPixmap.fromImage(images[4]))
			self.canvasBuffer_4.setAlignment(QtCore.Qt.AlignCenter)

	def initUI(self):
		self.setGeometry(200, 200, 600, 720)
		self.setWindowTitle("Data Lens")

		self.canvas = QtWidgets.QLabel(self)
		self.canvas.resize(600, 600)
		self.canvas.move(0, 120)
		self.setPhoto()

		self.canvasBuffer_0 = QtWidgets.QLabel(self)
		self.canvasBuffer_0.resize(120, 120) 
		self.canvasBuffer_0.move(0, 0)

		self.canvasBuffer_1 = QtWidgets.QLabel(self)
		self.canvasBuffer_1.resize(120, 120) 
		self.canvasBuffer_1.move(120, 0)

		self.canvasBuffer_2 = QtWidgets.QLabel(self)
		self.canvasBuffer_2.resize(120, 120) 
		self.canvasBuffer_2.move(240, 0)

		self.canvasBuffer_3 = QtWidgets.QLabel(self)
		self.canvasBuffer_3.resize(120, 120) 
		self.canvasBuffer_3.move(360, 0)

		self.canvasBuffer_4 = QtWidgets.QLabel(self)
		self.canvasBuffer_4.resize(120, 120) 
		self.canvasBuffer_4.move(480, 0)
		self.setBuffer()

		self.close_button = QtWidgets.QPushButton(self)
		self.close_button.setText("Close")
		self.close_button.resize(200, 50)
		self.close_button.move(200, 670)
		self.close_button.clicked.connect(self.close)

		self.next_button = QtWidgets.QPushButton(self)
		self.next_button.setText(u"\u02C3")
		self.next_button.resize(40, 40)
		self.next_button.move(560, 40)
		self.next_button.setFont(QFont('Arial', 15))
		self.next_button.clicked.connect(self.nextPhoto)

		self.previous_button = QtWidgets.QPushButton(self)
		self.previous_button.setText(u"\u02C2")
		self.previous_button.resize(40, 40)
		self.previous_button.move(0, 40)
		self.previous_button.setFont(QFont('Arial', 15))
		self.previous_button.clicked.connect(self.previousPhoto)

	def update(self):
		self.label.adjustSize()

# TO BE ADDED IN visualise.py
# def window():
# 	app = QApplication(sys.argv)
# 	win = AppWindow()
# 	win.show()
# 	sys.exit(app.exec_())

# window()