from flask_apscheduler import APScheduler
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Kanji as kanji
import Mics
from datetime import date

fdate = date.today().strftime('%d/%m/%Y')

app = Flask(__name__)



# function executed by scheduled job
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
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
            toSend_kanji[3] + '\n' + toSend_kanji[4]+ '\n\n\n')
    img = Mics.KanjiTestAnswerImageUrl(fdate, toSend_meaning, toSend_hiragana)
    msg.media(img)
    responded = True
    if not responded:
        msg.body('Im sorry I did not understand your last reply')
    return str(resp)


if (__name__ == "__main__"):
    scheduler = APScheduler()
    scheduler.add_job(func=bot, args=['job run'], trigger='interval', id='job', seconds=5)
    scheduler.start()
    app.run(port=8000)
