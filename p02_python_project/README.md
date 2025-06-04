# Program to demonstrate integration with GitHub
### To fetch details of the Users who created Pull requests(Active) on Kubernetes Github repo.

## Steps:
### Step 1:
Github URL to fetch live pull requests from the GitHub API

### Step2: 
Make a GET request to fetch pull requests data from the GitHub API

### Step3:
- Only if the response is successful [Else exit & jump to step 6 and return error code ]
- Convert the JSON response to a dictionary

### Step 4: 
Create an empty dictionary to store PR creators and their counts

### Step 5:    
Iterate through each pull request and extract the creator's name

### Step 6:
#### Results
- Display the dictionary of PR creators and their counts
