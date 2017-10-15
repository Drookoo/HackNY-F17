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
    precinct_zip = []
    url = 'http://webpage.pace.edu/ar88230p/meow.json'
    url2 = 'https://data.cityofnewyork.us/resource/qiz3-axqb.json'
    precinct_data = requests.get(url2).json()
    #https://data.cityofnewyork.us/Public-Safety/FDNY-Firehouse-Listing/hc8x-tcnd
    #https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95
    dataset = requests.get(url).json()

    for e in range(213):
        zipcode.append(dataset[e]['postcode'])

    for e in range(1000):
        if 'zip_code' in precinct_data[e]:
            precinct_zip.append(precinct_data[e]['zip_code'])

    if message_body not in zipcode:
        resp.message("your zipcode is not within the realm "
                     "of new york city")
    else:
        if message_body == '10002':
            sum = int(zipcode.count(str(10009))) + int(zipcode.count(str(10012)) + int(
                zipcode.count(str(10013))) + int(zipcode.count(str(10003))) + int(
                zipcode.count(str(10007))) + int(zipcode.count(str(10038))))
        elif message_body == '10003':
            sum = int(zipcode.count(str(10002))) + int(zipcode.count(str(10009)) + int(
                zipcode.count(str(10010))) + int(zipcode.count(str(100011))) + int(
                zipcode.count(str(10012))))
        elif message_body == '10004':
            sum = int(zipcode.count(str(10006))) + int(zipcode.count(str(10005)))
        elif message_body == '10005':
            sum = int(zipcode.count(str(10004))) + int(
                zipcode.count(str(10006)) + int(zipcode.count(str(10007))) + int(zipcode.count(str(10038))))
        resp.message(
            'Your requested zipcode has {} fire stations and {} '
            'fire stations in neighboring postal codes. Over the last'
            '1000 incidents, your zipcode, {}, has had {} occurences of '
            'motor vehicle collisions'.format(
                zipcode.count(message_body), sum, message_body, precinct_zip.count(message_body)))


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