# Read More: https://docs.python-requests.org/en/master/
# pip install requests

import requests

response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code) # 404


response = requests.get("https://api.open-notify.org/astros.json")
responseRawSocket = response.raw
responseJson = response.json() # Serializes the string result into JSON object.

#### Process Response Stream ####
with open(filename, 'wb') as fileStream:
    for chunk in response.iter_content(chunk_size = 128):
        fileStream.write(chunk)

headers = {
  'user-agent': 'my-app/0.0.1'
}
        
parameters = {
  "lat": 40.71,
  "lon": -74
}
response = requests.get("https://api.open-notify.org/iss-pass.json", headers = headers, params = parameters)

#### POST Request ####
payload = {
  'key1': 'value1',
  'key2': 'value2'
}

response = requests.post("https://httpbin.org/post", data = payload)
