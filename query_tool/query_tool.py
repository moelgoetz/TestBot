#!/usr/bin/env python3
#
#
#

import requests


#
#
#
def ask_duck_duck_go(url, query_string):
    return requests.get(url, {'q': query_string})


#
#
#
if __name__ == "__main__":
    print('Hello World')
    # https://duckduckgo.com/?q=indiana+university
    print(ask_duck_duck_go('https://duckduckgo.com/', 'indiana+university').text)
