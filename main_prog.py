import sys
import vlc
import translate
import textToSpeech
import speechToText
import playsound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QLCDNumber, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QComboBox, QFileDialog
from tkinter.filedialog import askopenfilename


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def sttui(self):  # Speech to text button function
        if str((self.chln1).currentText()) == 'Русский':
            self.name_input.setText(speechToText.speech_to_text(False, 'ru'))
        elif str((self.chln1).currentText()) == 'English':
            self.name_input.setText(speechToText.speech_to_text(False, 'en'))
        self.name_output.setText(translate.text_to_text(
            (self.name_input).text(),
            (self.chln2).currentText(),
            (self.chln1).currentText()))

    def tr_btn(self):
        self.name_output.setText(translate.text_to_text(
            (self.name_input).text(),
            (self.chln2).currentText(),
            (self.chln1).currentText()))

    def tts_func(self):  # Play button function
            textToSpeech.text_to_text((self.name_output).text(),
                                      (self.chln2).currentText())
            playsound.playsound('text_on_another_lang.mp3', True)
            sys.exit(app.exec_())

    def only_save(self):
        textToSpeech.text_to_text((self.name_output).text(),
                                  (self.chln2).currentText())
        sys.exit(app.exec_())

    def initUI(self):  # User Interface
        self.setFixedSize(400, 268)
        self.setWindowTitle('Speech-To-Speech')
        self.setWindowIcon(QIcon('icon.ico'))
        self.text_input()
        self.text_output()
        self.choose_language()
        self.save_audio()
        self.save_play_audio()
        self.from_mic()
        self.translate_btn()

    def save_play_audio(self):  # Save and play button
        play = QPushButton('Сохранить, озвучить и закрыть', self)
        play.resize(180, 25)
        play.move(64, 185)
        play.clicked.connect(self.tts_func)

    def save_audio(self):  # Save button
        play = QPushButton('Сохранить и закрыть', self)
        play.resize(180, 25)
        play.move(64, 210)
        play.clicked.connect(self.only_save)

    def translate_btn(self):  # Translate button
        play = QPushButton('Перевести', self)
        play.resize(140, 25)
        play.move(64, 100)
        play.clicked.connect(self.tr_btn)

    def from_mic(self):  # From mic button
        micbtn = QPushButton('С микрофона', self)
        micbtn.resize(150, 25)
        micbtn.move(220, 68)
        micbtn.clicked.connect(self.sttui)

    def text_input(self):  # Text input line
        label = QLabel(self)
        label.setText("Введите ваше слово на                           :")
        label.move(70, 50)

        self.name_input = QLineEdit(self)
        self.name_input.move(65, 70)
        self.name_input.resize(150, 23)

    def text_output(self):  # Text output line
        label = QLabel(self)
        label.setText("Вот ваше слово на                          :")
        label.move(70, 140)

        self.name_output = QLineEdit(self)
        self.name_output.move(65, 160)
        self.name_output.resize(150, 23)

    def choose_language(self):  # Choose language box
        self.chln1 = QComboBox(self)
        self.chln1.addItems(['Русский', 'English'])
        self.chln1.move(195, 45)

        self.chln2 = QComboBox(self)
        self.chln2.addItems(['English', 'Русский'])
        self.chln2.move(170, 135)


try:
    if __name__ == '__main__':  # Calling UI
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())
except:
    pass
