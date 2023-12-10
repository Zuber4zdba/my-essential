import requests

def get_merged_branches(token, owner, repo_name):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    merged_branches_url = f"https://api.github.com/repos/{owner}/{repo_name}/branches?protected=true"

    response = requests.get(merged_branches_url, headers=headers)

    if response.status_code == 200:
        merged_branches = [branch['name'] for branch in response.json()]
        return merged_branches
    else:
        print(f"Failed to get merged branches. Status code: {response.status_code}, "
              f"Message: {response.json()['message']}")
        return None

# Replace 'YOUR_GITHUB_TOKEN', 'OWNER', and 'REPO_NAME' with your actual values
token = "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"
owner = "zuber4zdba"
repo_name = "my-essential"

merged_branches = get_merged_branches(token, owner, repo_name)

if merged_branches is not None:
    print("Merged branches in the repository:")
    for branch in merged_branches:
        print(merged_branches)
else:
    print("Unable to retrieve merged branches.")
