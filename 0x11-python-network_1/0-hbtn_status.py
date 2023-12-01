#!/usr/bin/python3
"""
 Fetches a url and displays the response
"""
import urllib.request

if __name__ == "__main__":
    r = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(r) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
