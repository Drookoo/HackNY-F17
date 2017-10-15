import requests
from collections import Counter
zipcode = []
dreamset = []

url = 'http://webpage.pace.edu/ar88230p/meow.json'
dataset = requests.get(url).json()
address = []
boro = []
message_body = input('zip: ')
for e in range(213):
   zipcode.append(dataset[e]['postcode'])
   address.append(dataset[e]['facilityaddress'])
   boro.append(dataset[e]['borough'])
if message_body == '10002':
    sum = int(zipcode.count(str(10009))) + int(zipcode.count(str(10012)) + int(
        zipcode.count(str(10013)))+ int(zipcode.count(str(10003)))+ int(
        zipcode.count(str(10007)))+ int(zipcode.count(str(10038))))
    print(sum)
elif message_body == '10003':
    sum = int(zipcode.count(str(10002))) + int(zipcode.count(str(10009)) + int(
        zipcode.count(str(10010)))+ int(zipcode.count(str(100011)))+ int(
        zipcode.count(str(10012))))
    print(sum)
elif message_body == '10004':
    sum = int(zipcode.count(str(10006))) + int(zipcode.count(str(10005)))
    print(sum)
elif message_body == '10005':
    sum = int(zipcode.count(str(10004))) + int(zipcode.count(str(10006)) + int(zipcode.count(str(10007)))+ int(zipcode.count(str(10038))))
    print(sum)