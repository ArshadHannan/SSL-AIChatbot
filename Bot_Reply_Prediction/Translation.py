from googletrans import Translator


def sinhala_english(userText):

    translator = Translator()
    text = userText

    source_lan = "sinhala"
    translated_to = "en"

    # translate text
    translated_text = translator.translate(text, src=source_lan, dest=translated_to)
    print(f"The Actual Text was {text}")
    print(f"The Translated Text is: {translated_text.text}")
    print(f"The Translated Text pronunciation is {translated_text.pronunciation}")

    translated_eng_text = translated_text.text

    return translated_eng_text

def english_sinhala(bot_reply):

    translator = Translator()
    text = bot_reply

    source_lan = "en"
    translated_to = "si"

    # translate text
    translated_text = translator.translate(text, src=source_lan, dest=translated_to)
    print(f"The Actual Text was {text}")
    print(f"The Translated Text is: {translated_text.text}")
    print(f"The Translated Text pronunciation is {translated_text.pronunciation}")

    translated_sin_text = translated_text.text

    return translated_sin_text