import requests

pulls=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")


#print(pulls) ##This gives json output

#print(pulls.json()) ##This converts json to dictionary

#variable stores dictionary
details=pulls.json() 

#print(pulls.json()[0]["id"]
#print(pulls.json()[0]["user"]["login"]) ##Getting data from dictionary

for i in range(len(details)):
    print(details[i]["user"]["login"])
