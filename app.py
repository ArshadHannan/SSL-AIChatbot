from flask import Flask, render_template, request
from Bot_Reply_Prediction.Bot_Prediction import chatbot_response
from Bot_Reply_Prediction.Translation import sinhala_english, english_sinhala, Translator
from SSL_Prediction.Prediction import prediction

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)

    translator = Translator()
    tanslated_lang = translator.detect(userText).lang

    sinhala_sign = "si"

    if tanslated_lang == sinhala_sign:
        translated_user_text = sinhala_english(userText)
        bot_reply = chatbot_response(translated_user_text)
        print("bot reply:"+bot_reply)
        translated_bot_text = english_sinhala(bot_reply)
        return translated_bot_text

    else:
        bot_reply = chatbot_response(userText)
        return bot_reply

@app.route("/predictedText", methods = ['POST'])
def get_prediction_response():
    prediction1 = prediction()
    # prediction1 = "deaf and mute population in srilanka"
    print(prediction1)
    traslated = english_sinhala(prediction1)

    return {"data":traslated}


if __name__ == "__main__":
    app.run()