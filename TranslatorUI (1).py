import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QComboBox, QFileDialog
from tkinter.filedialog import askopenfilename

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setFixedSize(590, 350)
        self.setWindowTitle('')
        self.text_input()
        self.text_output()
        self.choose_language()
        self.audio_input_ckeck()
        self.button_select_file()
        self.play_audio()


    def audio_input_ckeck(self):
        cb = QCheckBox('С микрофона', self)
        cb.move(250, 110)

    def play_audio(self):
        play1 = QPushButton('Воспроизвести', self)
        play1.resize(100, 25)
        play1.move(115, 135)

        play2 = QPushButton('Воспроизвести', self)
        play2.resize(100, 25)
        play2.move(115, 225)

    def button_select_file(self):
        label = QLabel(self)
        label.setText("или выберите файл")
        label.move(337, 112)

        btn = QPushButton('...', self)
        btn.resize(25, 25)
        btn.move(440, 105)
        btn.clicked.connect(self.selectFile)
        
    def selectFile(self):
        self.selected_file = QFileDialog.getOpenFileName()

    def text_input(self):
        label = QLabel(self)
        label.setText("Введите ваше слово на                           :")
        label.move(110, 90)

        self.name_input = QLineEdit(self)
        self.name_input.move(105, 110)

    def text_output(self):
        label = QLabel(self)
        label.setText("Вот ваше слово на                          :")
        label.move(110, 180)

        self.name_output = QLineEdit(self)
        self.name_output.move(105, 200)

    def choose_language(self):
        self.chln1 = QComboBox(self)
        self.chln1.addItems(['Русский', 'English'])
        self.chln1.move(235, 85)

        self.chln2 = QComboBox(self)
        self.chln2.addItems(['Русский', 'English'])
        self.chln2.move(210, 175)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    ex.show()
    sys.exit(app.exec())
