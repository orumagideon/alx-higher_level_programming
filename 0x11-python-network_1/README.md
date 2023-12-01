# Python Network Scripts

This repository contains Python scripts for handling network-related tasks using different libraries such as `urllib` and `requests`. Each script corresponds to a specific network operation.

## Scripts Overview

### 0-hbtn_status.py

- Fetches https://alx-intranet.hbtn.io/status using `urllib`.
- Displays the body of the response in a specific format.

### 1-hbtn_header.py

- Takes a URL, sends a request, and displays the value of the X-Request-Id variable from the response header using `urllib` and `sys`.

### 2-post_email.py

- Sends a POST request with an email parameter to a specified URL using `urllib`.
- Displays the body of the response (decoded in utf-8).

### 3-error_code.py

- Fetches a URL and displays the body of the response.
- Handles urllib.error.HTTPError exceptions and prints the corresponding HTTP status code.

### 4-hbtn_status.py

- Fetches https://alx-intranet.hbtn.io/status using `requests`.
- Displays the body of the response in a specific format.

### 5-hbtn_header.py

- Takes a URL, sends a request, and displays the value of the X-Request-Id variable from the response header using `requests` and `sys`.

### 6-post_email.py

- Sends a POST request with an email parameter to a specified URL using `requests`.
- Displays the body of the response.

### 7-error_code.py

- Fetches a URL and displays the body of the response.
- Prints an error message if the HTTP status code is greater than or equal to 400.

### 8-json_api.py

- Sends a POST request with a letter parameter to http://0.0.0.0:5000/search_user using `requests`.
- Processes the response body in JSON format and displays specific information.

### 10-my_github.py

- Uses Basic Authentication with a personal access token to access GitHub API and displays the user's id.
- Takes GitHub credentials (username and personal access token) as arguments.

### 100-github_commits.py

- Fetches and displays 10 recent commits of a specified repository and owner using the GitHub API.
- Takes the repository name and owner name as arguments.

## Usage

Each script contains instructions on how to execute it along with usage examples.

## Testing

Scripts are tested in a sandbox environment provided, using specific servers and ports mentioned in the descriptions.

## Note

Be aware of rate limits for unauthenticated requests on GitHub API.
