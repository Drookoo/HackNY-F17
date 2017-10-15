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

    zipcode = []
    dreamset = {}
    url = 'https://data.cityofnewyork.us/resource/byk8-bdfw.json'
    dataset = requests.get(url).json()
    for e in range(47):
        zipcode.append(dataset[e]['postcode'])


    resp.message('There are {} fire stations in your zip'.format(zipcode.count(message_body)))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)