import speech_recognition as sr  # Импортируем распознавание голоса


def speechToText(flag, lang, path=''):
    r = sr.Recognizer()  # Инициализируем распознаватель голоса
    if path != '' or path != ' ' or path != '\t':
        open_file = sr.AudioFile(path)  # Открываем файл
        audio = r.record(open_file)
    else:
        if flag is False:
            with sr.Microphone() as source:
                audio = r.listen(source)  # Прослушиваем микрофон
    try:
        lng = ''  # Параметр языка для google
        if lang == 'ru':
            lng = 'ru-RU'  # Русский язык
        elif lang == 'en':
            lng = 'en-EN'  # Английский язык
        return(r.recognize_google(audio, language=lng))
        # Возвращаем распознанный текст
    except sr.UnknownValueError:  # Ошибка распознавания
        pass
    except sr.RequestError as e:  # Ошибка запроса к сервису
        pass
