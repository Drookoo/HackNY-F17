import requests
from collections import Counter
url = 'https://data.cityofnewyork.us/resource/qiz3-axqb.json'
precinct_data = requests.get(url).json()

message_body = input('yo ')
precinct_zip = []
print(precinct_data[0]['zip_code'])

for e in range(1000):
    if 'zip_code' in precinct_data[e]:
        precinct_zip.append(precinct_data[e]['zip_code'])

print(precinct_zip.count(message_body))
# print(Counter(precinct_zip))
#11207 has a ton of accidents

