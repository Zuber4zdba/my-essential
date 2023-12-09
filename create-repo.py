import requests

def create_github_repo(token, repo_name, description=""):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "name": repo_name,
        "description": description,
        "auto_init": True  # Initialize with a README file
    }

    url = "https://api.github.com/user/repos"
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully. status code: {response.status_code}")
    else:
        print(f"Failed to create repository. Status code: {response.status_code}, Message: {response.json()['message']}")

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
token = "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"
repo_name = "my-essential"
description = "all essential file scripts python code kube commands and all"

create_github_repo(token, repo_name)
