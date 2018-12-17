from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20181216T165708Z.256f02815004a360.907b12c1d0b00c3d0555378e945df82d09824dd2')


def text_to_text(text, lang_to, lang_from):
    if lang_to=='English':
        lang_to_y='en'
    elif lang_to=='Русский':
        lang_to_y='ru'
    if lang_from=='English':
        lang_from_y='en'
    if lang_from=='Русский':
        lang_from_y='ru'
    return(translate.translate(text, lang_from_y+'-'+lang_to_y).get('text')[0])
