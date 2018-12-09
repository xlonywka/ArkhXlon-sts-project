import translate_func  # Импортируем переводчик


google_translate = translate_func.Translator()  # Инициализируем переводчик


def text_to_text(text, lang_to):
    '''
    First param was text to translate.
    Second param is the language to be translated.
    :Example:
    >>> text_to_text('собака', 'en')
    'dog' was returned
    '''
    return(google_translate.translate(text, lang_to))
