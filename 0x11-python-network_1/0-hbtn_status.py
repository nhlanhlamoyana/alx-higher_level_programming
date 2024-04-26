#!/usr/bin/python3
'''a Python script that fetches https://alx-intranet.hbtn.io/status'''


if __name__ == '__main__':
    import urlib.request

    with urlib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
