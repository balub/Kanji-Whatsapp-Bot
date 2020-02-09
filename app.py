from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Kanji as kanji
import Mics
from datetime import date

fdate = date.today().strftime('%d/%m/%Y')
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'test' in incoming_msg:
        data = kanji.get5Kanji()
        toSend_kanji = []
        toSend_hiragana = []
        toSend_meaning = []
        for dat in data:
            toSend_kanji.append(dat['kanji'])
            toSend_hiragana.append(dat['hiragana'])
            toSend_meaning.append(dat['word'])
        msg.body(
            'Kanji for ' + fdate + '\n\n' + toSend_kanji[0] + '\n' + toSend_kanji[1] + '\n' + toSend_kanji[2] + '\n' +
            toSend_kanji[3] + '\n' + toSend_kanji[4] + '\n\n\n')
        img = Mics.KanjiTestAnswerImageUrl(fdate, toSend_meaning, toSend_hiragana)
        msg.media(img)
        responded = True
    if 'quiz' in incoming_msg:
        data,num = kanji.getXKanji(incoming_msg)
        toSend_kanji = []
        for dat in data:
            toSend_kanji.append(dat['kanji'])
        msg.body('Test Your Kanji' + '\n\n')
        for n in range(len(toSend_kanji)):
            msg.body(toSend_kanji[n])
        responded = True
    if not responded:
        msg.body('Im sorry I did not understand your last reply')
    return str(resp)


if __name__ == '__main__':
    app.run()
