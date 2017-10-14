from flask import Flask
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

client = Client('AC2f71f255524180a45b9acf3a55766db6', '69aa8e008a80ce5248f72429b5756fa5')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    zipcode = []
    url = 'https://data.cityofnewyork.us/resource/byk8-bdfw.json'
    dataset = requests.get(url).json()
    for e in dataset:
        zipcode.append('"postcode"')
    print(zipcode)


    resp = MessagingResponse()
    resp.message("Hello, Angel")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)