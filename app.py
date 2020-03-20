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
    if num_questions is 2:
        return level, default
    else:
        return level, split_sentence[2]


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    level, num_questions = process(data)




    # if not responded:
    #     msg.body('Im sorry I did not understand your last reply')
    return str(resp)


if __name__ == '__main__':
    app.run()
