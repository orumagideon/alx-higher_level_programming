#!/usr/bin/python3
"""
This script executes a POST request to http://0.0.0.0:5000/search_user.
It includes a specified letter as the 'q' parameter. If no letter is provided,
the 'q' parameter defaults to an empty string.
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        json_resp = response.json()
        if json_resp == {}:
            print("No results")
        else:
            print("[{}] {}".format(json_resp.get('id'), json_resp.get('name')))
    except ValueError:
        print("Invalid JSON format")
