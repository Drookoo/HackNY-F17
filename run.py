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
        elif message_body == '10001':
            sum = int(zipcode.count(str(10011)) + int(zipcode.count(str(10010)) + int(zipcode.count(str(10016)) + int(zipcode.count(str(10018))))))
        elif message_body == '10003':
            sum = int(zipcode.count(str(10002))) + int(zipcode.count(str(10009)) + int(
                zipcode.count(str(10010))) + int(zipcode.count(str(100011))) + int(
                zipcode.count(str(10012))))
        elif message_body == '10004':
            sum = int(zipcode.count(str(10006))) + int(zipcode.count(str(10005)))
        elif message_body == '10005':
            sum = int(zipcode.count(str(10004))) + int(
                zipcode.count(str(10006)) + int(zipcode.count(str(10007))) + int(zipcode.count(str(10038))))
        elif message_body == '10006':
            sum = int(zipcode.count(str(10007))) + int(zipcode.count(str(10005)) + int(zipcode.count(str(10004))) + int(
                zipcode.count(str(10048))) + int(zipcode.count(str(100038))))
        elif message_body == '10007':
            sum = int(zipcode.count(str(10013))) + int(zipcode.count(str(10038)) + int(zipcode.count(str(10006))) + int(
                zipcode.count(str(10048))))
        elif message_body == '10009':
            sum = int(zipcode.count(str(10010))) + int(zipcode.count(str(10003)) + int(zipcode.count(str(10002))))
        elif message_body == '10010':
            sum = int(zipcode.count(str(10016))) + int(zipcode.count(str(10001)) + int(zipcode.count(str(10011))) + int(
                zipcode.count(str(10011))) + int(zipcode.count(str(10003)) + int(zipcode.count(str(10009)))))
        elif message_body == '10012':
            sum = int(zipcode.count(str(10011))) + int(zipcode.count(str(10003)) + int(zipcode.count(str(10002))) + int(
                zipcode.count(str(10013) + zipcode.count(str(10014)))))
        elif message_body == '10035':
            sum = int(zipcode.count(str(10037))) + int(
                zipcode.count(str(10027)) + int(zipcode.count(str(10026))) + int(zipcode.count(str(10029))))
        elif message_body == '10037':
            sum = int(zipcode.count(str(10035))) + int(zipcode.count(str(10027))) + int(zipcode.count(str(10030)))
        elif message_body == '10030':
            sum = int(zipcode.count(str(10039))) + int(zipcode.count(str(10037))) + int(zipcode.count(str(10027))) + int(zipcode.count(str(10031))) + int(
                zipcode.count(str(10039)))
        elif message_body == '10039':
            sum = int(zipcode.count(str(10032))) + int(zipcode.count(str(10030)) + int(zipcode.count(str(10031))))
        elif message_body == '10032':
            sum = int(zipcode.count(str(10033))) + int(zipcode.count(str(10039))) + int(zipcode.count(str(10031)))
        elif message_body == '10033':
            sum = int(zipcode.count(str(10040))) + int(
                zipcode.count(str(10032)))
        elif message_body == '10040':
            sum = int(zipcode.count(str(10034))) + int(
                zipcode.count(str(10033)))
        elif message_body == '10034':
            sum = int(zipcode.count(str(10040)))
        elif message_body == '10031':
            sum = int(zipcode.count(str(10032))) + int(
                zipcode.count(str(10039))) + int(zipcode.count(str(10030))) + int(zipcode.count(str(10027)))
        elif message_body == '10027':
            sum = int(zipcode.count(str(10031))) + int(zipcode.count(str(10030))) + int(zipcode.count(str(10037))) + int(zipcode.count(str(10035))) + int(zipcode.count(str(10026))) + int(zipcode.count(str(10025)))
        elif message_body == '10026':
            sum = int(zipcode.count(str(10027))) + int(
                zipcode.count(str(10035))) + int(zipcode.count(str(10029))) + int(zipcode.count(str(10025)))
        elif message_body == '10025':
            sum = int(zipcode.count(str(10027))) + int(
                zipcode.count(str(10026))) + int(zipcode.count(str(10024)))
        elif message_body == '10024':
            sum = int(zipcode.count(str(10025))) + int(
                zipcode.count(str(10023)))
        elif message_body == '10023':
            sum = int(zipcode.count(str(10024))) + int(
                zipcode.count(str(10019)))
        elif message_body == '10019':
            sum = int(zipcode.count(str(10023))) + int(
                zipcode.count(str(10022))) + int(zipcode.count(str(10036)))
        elif message_body == '10036':
            sum = int(zipcode.count(str(10019))) + int(
                zipcode.count(str(10017))) + int(zipcode.count(str(10018)))
        elif message_body == '10018':
            sum = int(zipcode.count(str(10036))) + int(
                zipcode.count(str(10017))) + int(zipcode.count(str(10016))) + int(zipcode.count(str(10001)))
        elif message_body == '10016':
            sum = int(zipcode.count(str(10010))) + int(
                zipcode.count(str(10001))) + int(zipcode.count(str(10018))) + int(zipcode.count(str(10017)))
        elif message_body == '10029':
            sum = int(zipcode.count(str(10128))) + int(
                zipcode.count(str(10026))) + int(zipcode.count(str(10035)))
        elif message_body == '10128':
            sum = int(zipcode.count(str(10029))) + int(
                zipcode.count(str(10028)))
        elif message_body == '10021':
            sum = int(zipcode.count(str(10028))) + int(
                zipcode.count(str(10022)))
        elif message_body == '10022':
            sum = int(zipcode.count(str(10017))) + int(
                zipcode.count(str(10019))) + int(zipcode.count(str(10021)))
        elif message_body == '10017':
            sum = int(zipcode.count(str(10016))) + int(
                zipcode.count(str(10018))) + int(zipcode.count(str(10036))) + int(zipcode.count(str(10022)))

        resp.message(
            'Your requested zipcode has {} fire stations and {} '
            'fire stations in neighboring postal codes. Over the last '
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