#!/bin/bash

# Sending a PUT request to the specified URL
curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
