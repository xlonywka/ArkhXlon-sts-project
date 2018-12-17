from gtts import gTTS


def text_to_text(text1, lang_to):
    # Первый элемент текст, второй - язык для считывания
    if lang_to == 'Русский':
        tts = gTTS(text=text1, lang='ru')
        tts.save("text_on_another_lang.mp3")
    if lang_to == 'English':
        tts = gTTS(text=text1, lang='en')
        tts.save("text_on_another_lang.mp3")
