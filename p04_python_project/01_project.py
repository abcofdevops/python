# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

API_TOKEN="xxxxxxxxxxxxxxxxx"
email="abcofdevops@gmail.com"
username="abcofdevops"

url = f"https://{username}.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(email, API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output= json.loads(response.text)
name = output[0]["name"]
print(name)

print("\nOutput1")
names = [item["name"] for item in output]
print(names)
print("\nOutput1.1")
print(*names, sep="\n")

print("\nOutput2")
for item in output:
    print(item["name"])

print("\nOutput3")
names = []
for item in output:
    names.append(item["name"])
print(names)


