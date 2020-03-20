from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Kanji as kanji
import Mics
from datetime import date

fdate = date.today().strftime('%d/%m/%Y')
app = Flask(__name__)


def process(data):
    default = 20
    split_sentence = data.split()
    level = split_sentence[0]
    num_questions = len(split_sentence)
    if num_questions == 2:
        return level, default
    else:
        return level, split_sentence[2]


def listToString(s):
    str1 = ","
    return str1.join(s)


def N5Content(question_num):
    data = kanji.getKanji('n5', question_num)
    toSend_kanji = []
    toSend_hiragana = []
    toSend_meaning = []
    for dat in data:
        toSend_kanji.append(dat['kanji'])
        toSend_hiragana.append(dat['hiragana'])
        toSend_meaning.append(dat['word'])
    answers_hiragana_url = Mics.GenImageUrl(listToString(toSend_hiragana))
    answers_meaning_url = Mics.GenImageUrl(listToString(toSend_meaning))
    return toSend_kanji,answers_hiragana_url,answers_meaning_url


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    first_text, num_questions = process(incoming_msg)

    if first_text == "n5":
        msg.body(f"Wanted {num_questions} N5 kanji")
        dataFull,H_url,M_url = N5Content(num_questions)
        for data in dataFull:
            msg.body(data)
            msg.body("\n")
            msg.body(H_url)
            msg.body("\n")
            msg.body(M_url)
            msg.body("\n")
        responded = True
    elif first_text == "n4":
        msg.body(f"Wanted {num_questions} N4 kanji")
        responded = True
    elif first_text == "n3":
        msg.body(f"Wanted {num_questions} N3 kanji")
        responded = True
    elif first_text == "quiz":
        msg.body("Quiz")
        responded = True
    elif first_text == "leader":
        msg.body("Leader quiz")
        responded = True

    if not responded:
        msg.body('Im sorry I did not understand your last reply')
    return str(resp)


if __name__ == '__main__':
    app.run()
