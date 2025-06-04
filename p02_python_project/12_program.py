import requests

url="https://api.github.com/repos/kubernetes/kubernetes/pulls"

response=requests.get(url)

if response.status_code==200:
    pull_requests=response.json()

    pr_creator={} #Empty Dictionary to store result-[User and count]

    for pull in range(len(pull_requests)):
        creator = pull_requests[pull]["user"]["login"]
        if creator in pr_creator:
            pr_creator[creator] += 1
        else:
            pr_creator[creator] = 1

    print("PR creator and counts")
    for creator,count in pr_creator.items():
        print(f"{creator} : {count} PR(s)")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")

