#!/usr/bin/python3
"""
 Sends URL request to the URL
and displays the value if X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)

    with urllib.request.urlopen(r) as response:
        headers = response.getheaders()
        header_dict = dict(headers)
        request_id = header_dict.get('X-Request-Id')
        print(request_id)
