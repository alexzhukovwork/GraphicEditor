import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()


    self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

    self.setGeometry(self.left, self.top, self.width, self.height)

    self.openFileNameDialog()
    self.openFileNamesDialog()
    self.saveFileDialog()

    self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()

    options |= QFileDialog.DontUseNativeDialog
    files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                            "All Files (*);;Python Files (*.py)", options=options)
    if files:
        print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)