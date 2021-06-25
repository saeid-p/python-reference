# Read More: https://docs.python-requests.org/en/master/
# pip install requests

import requests

#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
#print(response.status_code) # 404


response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
responseJson = response.json() # Serializes the string result into JSON object.
print(responseJson)

headers = {
  'user-agent': 'my-app/0.0.1'
}
        
parameters = {
  "lat": 40.71,
  "lon": -74
}
response = requests.get("https://jsonplaceholder.typicode.com/todos/1", headers = headers, params = parameters)

#### POST Request ####
payload = {
  'userId': 1,
  'id': 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = payload)