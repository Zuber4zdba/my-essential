import requests

def create_github_branch(token, owner, repo_name, base_branch, new_branch):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get the SHA of the base branch
    base_branch_url = f"https://api.github.com/repos/{owner}/{repo_name}/branches/{base_branch}"
    response = requests.get(base_branch_url, headers=headers)

    if response.status_code == 200:
        base_branch_sha = response.json()["commit"]["sha"]

        # Create a new branch based on the specified base branch
        create_branch_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/refs"
        data = {
            "ref": f"refs/heads/{new_branch}",
            "sha": base_branch_sha
        }

        create_branch_response = requests.post(create_branch_url, headers=headers, json=data)

        if create_branch_response.status_code == 201:
            print(f"Branch '{new_branch}' created successfully.")
        else:
            print(f"Failed to create branch. Status code: {create_branch_response.status_code}, "
                  f"Message: {create_branch_response.json()['message']}")
    else:
        print(f"Failed to get base branch information. Status code: {response.status_code}, "
              f"Message: {response.json()['message']}")

# Replace 'YOUR_GITHUB_TOKEN', 'OWNER', 'REPO_NAME', 'BASE_BRANCH', and 'NEW_BRANCH' with your actual values
token = "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"
owner = "Zuber4zdba"
repo_name = "my-essential"
base_branch = "main"
new_branch = "dev"

create_github_branch(token, owner, repo_name, base_branch, new_branch)
