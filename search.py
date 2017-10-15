import requests
from collections import Counter
zipcode = []
dreamset = {}

url = 'http://webpage.pace.edu/ar88230p/meow.json'
dataset = requests.get(url).json()
address = []
for e in range(213):
   zipcode.append(dataset[e]['postcode'])
   address.append(dataset[e]['facilityaddress'])

print(address)
print(Counter(zipcode))