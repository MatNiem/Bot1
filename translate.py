from googletrans import Translator


def translate_google(sentence, src, dest):
    translator = Translator()
    result = translator.translate(sentence, dest=dest, src=src)
    return f'{result.origin} -> {result.text}'
