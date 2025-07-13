#!/usr/bin/python

"""This file is part of Count Up Timer.

Count Up Timer is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Count Up Timer is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Count Up Timer. If not, see <http://www.gnu.org/licenses/>"""

import sys
import time
from CutUtilQt import *
from PyQt5 import QtWidgets, QtCore

class CutMainWindow(QtWidgets.QMainWindow):

	def __init__(self):
		#general initialization
		super().__init__()
		self.setWindowTitle("Count Up Timer")
		#private variables
		self._timeDisplay = TimeDisplay()
		self._controlPanel = ControlPanel()
		self._seconds = 0
		self._timer = QtCore.QTimer(self)
		self._timer.setInterval(1000)
		#ui building
		containerLayout = QtWidgets.QVBoxLayout()
		containerLayout.addLayout(self._timeDisplay)
		containerLayout.addLayout(self._controlPanel)
		self._centralWidget = QtWidgets.QWidget()
		self._centralWidget.setLayout(containerLayout)
		self.setCentralWidget(self._centralWidget)
		#event handling
		self.initializeSlots()
		#finally
		self.show()
	
	def initializeSlots(self):
		self._controlPanel.getStartButton().clicked.connect(self.onStartButtonClicked)
		self._controlPanel.getStopButton().clicked.connect(self.onStopButtonClicked)
		self._controlPanel.getResetButton().clicked.connect(self.onResetButtonClicked)
		self._timer.timeout.connect(self.onTimeout)
	
	def onStartButtonClicked(self):
		self._timer.start()

	def onStopButtonClicked(self):
		self._timer.stop()

	def onResetButtonClicked(self):
		self._seconds = 0
		self.displayTime()
	
	def onTimeout(self):
		self._seconds += 1
		self.displayTime()
		
	def displayTime(self):
		self._timeDisplay.setText(time.strftime('%H:%M:%S', time.gmtime(self._seconds)))

application = QtWidgets.QApplication(sys.argv)
cutMainWindow = CutMainWindow()
application.exec_()
