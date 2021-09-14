import sys
import os 
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize

from lanegui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("AIDrivers Automated Annotation")
		self.browse_button.clicked.connect(self.launchFileDialog)
		self.save_button.clicked.connect(self.saveFileDialog)
		self.help_button.clicked.connect(self.HelpDialog)
		self.faq_button.clicked.connect(self.FAQDialog)

	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename = QFileDialog.getExistingDirectory(self,"Select Save Directory","/home",options=options)
		if filename:
			print(filename)
			# self.file_label.setText(filename)
			self.outputterminal_textedit.setText(filename)

	def launchFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename, _ = QFileDialog.getOpenFileName(self,"Open Rosbag file", "","All Files (*);;Python Files (*.py)", options=options)
		if filename:
			print(filename)
			self.file_label.setText(filename)
			# self.outputterminal_textedit.setText(filename)

	def HelpDialog(self,s):
		dlg = QMessageBox(self)
		dlg.setWindowTitle("Help")
		dlg.setText("Help is here")
		dlg.exec_()

	def FAQDialog(self,s):
		dlg = QMessageBox(self)
		dlg.setWindowTitle("FAQ")
		dlg.setText("FAQ")
		dlg.exec_()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()