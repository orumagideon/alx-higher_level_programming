#!/usr/bin/python3
"""
 Script takes a URL and an email address
sends a post request to the URL with the email paramaters
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    response = requests.post(url, data=payload)
    body = response.text
    print(body)
