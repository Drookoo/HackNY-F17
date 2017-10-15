import requests
from collections import Counter
zipcode = []
dreamset = []

url = 'http://webpage.pace.edu/ar88230p/meow.json'
dataset = requests.get(url).json()
address = []
boro = []
for e in range(213):
   zipcode.append(dataset[e]['postcode'])
   address.append(dataset[e]['facilityaddress'])
   boro.append(dataset[e]['borough'])

# zipcode.count()
print(address[3])
print(zipcode[3])
print(boro[3])