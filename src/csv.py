import sys
from PySide.QtGui import QApplication, QWidget

from src import gui
import csv


class Csv(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.myForm = gui.Ui_Form()
        self.myForm.setupUi(self)
        self.myForm.el.clicked.connect(self.buttonHit)

    def read_csv(self):
        with open('test.csv', newline='') as file:
            txt = ""
            reader = csv.reader(file, delimiter=';', quotechar='|')
            for row in reader:
                txt += str(', '.join(row)) + "\n"

            self.myForm.tb.setText(txt)

    def buttonHit(self):
        self.read_csv()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Csv()
    frame.show()
    sys.exit(app.exec_())
