#!/bin/bash
# Script receives a url from the cli and then  display the size of the body of the response
curl -s "$1" | wc -c
