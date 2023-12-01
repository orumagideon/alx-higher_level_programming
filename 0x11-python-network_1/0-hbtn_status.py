#!/usr/bin/python3
"""
This script takes my GitHub credentials (username and password)
and uses GitHub API to display my ID.
We must use Basic Authentication with a Personal Access Token (PAT) as the password.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <PAT>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    pat = sys.argv[2]

    auth = HTTPBasicAuth(username, pat)
    response = requests.get("https://api.github.com/user", auth=auth)

    if response.status_code == 200:
        json_resp = response.json()
        user_id = json_resp.get('id')
        print(user_id)
    else:
        print("Failed to fetch user ID. Status code:", response.status_code)
