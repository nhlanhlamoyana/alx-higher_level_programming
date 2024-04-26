#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urlib.request


if __name__ == "__main__":
    request = urlib.request.Request("https://alx-intranet.hbtn.io/status")
    with urlib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
