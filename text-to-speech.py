from gtts import gTTS
import os


def speech(text1, lng):
    tts = gTTS(text=text1, lang=lng)
    tts.save("speech_on_another_language.mp3")
    os.system("mpg321 speech_on_another_language.mp3")
