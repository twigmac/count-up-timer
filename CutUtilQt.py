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

from PyQt4 import QtGui
from PyQt4 import QtCore

class TimeDisplay(QtGui.QHBoxLayout):

	def __init__(self):
		super(TimeDisplay, self).__init__() # See [1]
		self._lcd = QtGui.QLCDNumber()
		self._lcd.setNumDigits(8)
		self._text = "00:00:00"
		self.setText(self._text)
		self.addWidget(self._lcd)
	
	def setText(self, str):
		self._text = str
		self._lcd.display(QtCore.QString(str))
	
	def getText(self):
		return self._text

class ControlPanel(QtGui.QHBoxLayout):

	def __init__(self):
		super(ControlPanel, self).__init__() # See [1]
		self._startButton = QtGui.QPushButton("Start")
		self._stopButton = QtGui.QPushButton("Stop")
		self._resetButton = QtGui.QPushButton("Reset")
		self.addWidget(self._startButton)
		self.addWidget(self._stopButton)
		self.addWidget(self._resetButton)

	def getStartButton(self):
		return self._startButton

	def getStopButton(self):
		return self._stopButton

	def getResetButton(self):
		return self._resetButton


# [1] http://stackoverflow.com/questions/6002895/understanding-the-underlying-c-c-object-has-been-deleted-error/10889343#10889343
