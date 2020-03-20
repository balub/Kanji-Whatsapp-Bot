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
        return level, split_sentence[2],split_sentence[1]


def listToString(s):
    str1 = ""
    return str1.join(str(s))


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
    return toSend_kanji, answers_hiragana_url, answers_meaning_url


def N4Content(question_num):
    data = kanji.getKanji('n4', question_num)
    toSend_kanji = []
    toSend_hiragana = []
    toSend_meaning = []
    for dat in data:
        toSend_kanji.append(dat['kanji'])
        toSend_hiragana.append(dat['hiragana'])
        toSend_meaning.append(dat['word'])
    answers_hiragana_url = Mics.GenImageUrl(listToString(toSend_hiragana))
    answers_meaning_url = Mics.GenImageUrl(listToString(toSend_meaning))
    return toSend_kanji, answers_hiragana_url, answers_meaning_url


def N3Content(question_num):
    data = kanji.getKanji('n3', question_num)
    toSend_kanji = []
    toSend_hiragana = []
    toSend_meaning = []
    for dat in data:
        toSend_kanji.append(dat['kanji'])
        toSend_hiragana.append(dat['hiragana'])
        toSend_meaning.append(dat['word'])
    answers_hiragana_url = Mics.GenImageUrl(listToString(toSend_hiragana))
    answers_meaning_url = Mics.GenImageUrl(listToString(toSend_meaning))
    return toSend_kanji, answers_hiragana_url, answers_meaning_url


def QuizContent(level, question_num):
    data = kanji.getKanji(level, question_num)
    toSend_kanji = []
    toSend_hiragana = []
    toSend_meaning = []
    for dat in data:
        toSend_kanji.append(dat['kanji'])
        toSend_hiragana.append(dat['hiragana'])
        toSend_meaning.append(dat['word'])
    return toSend_kanji


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    first_text, num_questions,level = process(incoming_msg)

    if first_text == "n5":
        dataFull, H_url, M_url = N5Content(num_questions)
        for data in dataFull:
            msg.body(data)
            msg.body("\n")
        msg.body(f' The Answers in hiragana are {H_url}')
        msg.body("\n")
        msg.body(f' The Meaning of the Kanji {M_url}')
        msg.body("\n")
        responded = True
    elif first_text == "n4":
        dataFull, H_url, M_url = N4Content(num_questions)
        for data in dataFull:
            msg.body(data)
            msg.body("\n")
        msg.body(f' The Answers in hiragana are {H_url}')
        msg.body("\n")
        msg.body(f' The Meaning of the Kanji {M_url}')
        msg.body("\n")
        responded = True
    elif first_text == "n3":
        dataFull, H_url, M_url = N3Content(num_questions)
        for data in dataFull:
            msg.body(data)
            msg.body("\n")
        msg.body(f' The Answers in hiragana are {H_url}')
        msg.body("\n")
        msg.body(f' The Meaning of the Kanji {M_url}')
        msg.body("\n")
        responded = True
    elif first_text == "quiz":
        dataFull = QuizContent(level, num_questions)
        for data in dataFull:
            msg.body(data)
            msg.body("\n")
        responded = True
    elif first_text == "leader":
        msg.body("Leader quiz")
        responded = True

    if not responded:
        msg.body('Im sorry I did not understand your last reply')
    return str(resp)


if __name__ == '__main__':
    app.run()
