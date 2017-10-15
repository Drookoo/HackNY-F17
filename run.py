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
    url = 'http://webpage.pace.edu/ar88230p/meow.json'
    #https://data.cityofnewyork.us/Public-Safety/FDNY-Firehouse-Listing/hc8x-tcnd
    dataset = requests.get(url).json()

    for e in range(213):
        zipcode.append(dataset[e]['postcode'])

    if message_body not in zipcode:
        resp.message("your zipcode is not within the realm "
                     "of new york city")
    else:
        plusone = int(message_body) + 1
        minusone = int(message_body) - 1
        sum = zipcode.count(plusone) + zipcode.count(minusone)
        resp.message(
            'Your requested zipcode has {} fire stations and {} '
            'fire stations in neighboring postal codes'.format(
                zipcode.count(message_body), sum))


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, request
# from twilio.rest import Client
# from twilio.twiml.messaging_response import MessagingResponse
# from twilio import twiml
# import requests
#
# app = Flask(__name__)
#
# client = Client('AC2f71f255524180a45b9acf3a55766db6', '69aa8e008a80ce5248f72429b5756fa5')
#
# @app.route('/', methods=['GET', 'POST'])
# def sms():
#     message_body = request.form['Body']
#     resp = MessagingResponse()
#
#     zipcode = []
#     address = []
#     boro = []
#     url = 'http://webpage.pace.edu/ar88230p/meow.json'
#     dataset = requests.get(url).json()
#
#     for e in range(213):
#         zipcode.append(dataset[e]['postcode'])
#         address.append(dataset[e]['facilityaddress'])
#         boro.append(dataset[e]['borough'])
#
#     if message_body not in zipcode:
#         resp.message("gtfo feg._.")
#     else:
#         resp.message(
#             'There are {} fire stations {} in your {} zip'.format(zipcode.count(message_body), address[0], boro[0]))
#
#     return str(resp)
#
# if __name__ == "__main__":
#     app.run(debug=True)