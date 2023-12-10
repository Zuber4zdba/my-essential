import requests

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
    print("Branches in the repository:")
    for branch in branches:
        print(branch)
