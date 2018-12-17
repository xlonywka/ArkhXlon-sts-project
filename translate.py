from yandex_translate import YandexTranslate
keylong = '4a360.907b12c1d0b00c3d0555378e945df82d09824dd2'
translate = YandexTranslate('trnsl.1.1.20181216T165708Z.256f0281500' + keylong)


def text_to_text(text, lang_to, lang_from):
    # Переводчик. Первый элемент - текст
    # Второй - язык с которого переводить
    # Третий - Язык на который переводить
    if lang_to == 'English':
        lang_to_y = 'en'
    elif lang_to == 'Русский':
        lang_to_y = 'ru'
    if lang_from == 'English':
        lang_fy = 'en'
    if lang_from == 'Русский':
        lang_fy = 'ru'
    return(translate.translate(text, lang_fy + '-' + lang_to_y).get('text')[0])
