#!/usr/bin5/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  -Displays the body of the response.
  """
  if __name__ = '__main__':
  import sys
  import requests


      params = {'email': sys.argv[2]}
      res = requests.post(sys.argv[1], data=params)
      print(res.tex)
