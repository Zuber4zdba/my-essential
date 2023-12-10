import requests
import sys

def get_github_branches(token, repo_owner, repo_name):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    branches_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches"

    response = requests.get(branches_url, headers=headers)

    if response.status_code == 200:
        branches = [branch['name'] for branch in response.json()]
        return branches
    else:
        print(f"Failed to get branches. Status code: {response.status_code}, "
              f"Message: {response.json()['message']}")
        return None

# Replace 'YOUR_GITHUB_TOKEN', 'OWNER', and 'REPO_NAME' with your actual values
token = "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"
owner = "Zuber4zdba"
repo_name = "my-essential"

branches = get_github_branches(token, owner, repo_name)

if branches is not None:
    print("Branches in the repo '{repo_name}' is and also stored in file branches.txt")
    for branch in branches:
        print(branch)
        # open a file in write mode
    with open('branches.txt', 'w') as file:
        # write branches to the file
            for branch in branches:
                 file.write(branch + '\n')
    print("branches list has beed written to 'branches.txt'.")
else:
     print(f"unable to retrieve branches or there is no branch in repo '{repo_name}':")