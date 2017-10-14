from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import requests


app = Flask(__name__)

client = Client('AC2f71f255524180a45b9acf3a55766db6', '69aa8e008a80ce5248f72429b5756fa5')

@app.route('/', methods=['GET', 'POST'])
def sms():
    message_body = request.form['Body']
    resp = MessagingResponse()
    resp.message('Hello, your zip is {}'.format(message_body))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)