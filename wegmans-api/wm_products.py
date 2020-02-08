"""
Wegman Products API Wrapper
"""

#external packages
import requests
import json

#import authorization key from auth.py, hidden from git
from auth import API_KEY

#authorization header
header = '?api-version=2018-10-18&Subscription-Key=' + API_KEY
url = 'https://api.wegmans.io/products/'

print(API_KEY)

response = requests.get('https://api.wegmans.io/products/categories?api-version=2018-10-18&Subscription-Key=' + API_KEY)

print(response.json())
