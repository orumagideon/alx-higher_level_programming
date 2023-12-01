#!/usr/bin/python3
"""
 Sript sends a request to the URL and 
 displays  the body of the response
 Manage urllib.error.HTTPError exceptions and print the errorcode
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    r = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(r) as response:
            resp = response.read()
            print(resp.decode('ascii'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
