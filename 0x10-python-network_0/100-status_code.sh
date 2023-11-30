#!/bin/bash
# sends request to the URL
curl -s -o /dev/null/ -w "%{http_code}" "$1"
