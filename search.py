import requests
zipcode = []
url = 'https://data.cityofnewyork.us/resource/byk8-bdfw.json'
dataset = requests.get(url).json()
for e in range(47):
   zipcode.append(dataset[e]['postcode'])

print(zipcode)