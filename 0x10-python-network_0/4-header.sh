#!/bin/bash
# Request to the URL and displays the body of the response, a header var is also specified
curl -sH "X-School-User-ID: 98" "$1"
