import requests
from requests.exceptions import ConnectionError
import json
import os
import sys
usage = """
    Usage: Enter a url to shorten
    Example: python filename.py google.com
    """
def shorten():
    userUrl=input("Enter a url to shorten:") # Get user URL from command line argument
    try:
        response = requests.put("https://api.shorte.st/v1/data/url", {"urlToShorten":userUrl}, headers={"public-api-token": "fee07e5aeff511b07b1dd67e06fddffe"})
        shortened_url = json.loads(response.content.decode('utf-8'))
        print('Your Long URL is: '+userUrl+'\n\nYour Shortened URL is: '+shortened_url['shortenedUrl'])
    except ConnectionError as e:
        print (' Ensure you are connected to the internet')
if __name__ == '__main__':
    shorten()
    
