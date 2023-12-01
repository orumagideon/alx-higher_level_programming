#!/usr/bin/python3
"""
 Sends a URL request to it
and displays variable X-Request-Id
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    response_id = response.headers.get("X-Request-Id")
    print(response_id)
