#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""


import sys
import urlib.parse
import urlib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urlib.parse.urlencode(value).encode("ascii")

    request = urlib.request.Request(url, data)
    with urlib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
