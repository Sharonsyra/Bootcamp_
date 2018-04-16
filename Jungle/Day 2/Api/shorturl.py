import requests
from requests.exceptions import ConnectionError
import json
import os
import sys

usage = """

	Usage: python shortest.py URL link...

	Example: python shortest.py google.com

	"""

def shorten():
	if len(sys.argv) != 2:
		print (usage)
	else:
		userUrl = sys.argv[1] # Get user URL from command line argument
		try:
			response = requests.put("https://api.shorte.st/v1/data/url", {"urlToShorten":userUrl}, headers={"public-api-token": "fee07e5aeff511b07b1dd67e06fddffe"})
			shortened_url = json.loads(response.content)
			print('Long URL: '+userUrl+'\n\nShortened URL: '+shortened_url['shortenedUrl'])

		except ConnectionError as e:
			print (' Ensure you are connected to the internet')

if __name__ == '__main__':
	shorten()
