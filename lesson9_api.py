import json
from urllib.request import urlopen

api_key = "3343e1e9e073644065c5fc2f4b69fe03"
response = urlopen ('http://api.openweathermap.org/data/2.5/weather?q=Vienna&appid=' + api_key).read()
data = json.loads(response) # .decode('utf-8')
print(data)

print(data["weather"][0]["description"])

