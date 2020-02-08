"""
Wegmans Stores API Wrapper
Written at Brickhack 2020
author: Joshua Yoder <jpfyoder>
author: Dhaval Shrishrimal
"""

#external packages
import requests
import json

#import authorization key from auth.py, hidden from git
from auth import API_KEY

#authorization header and url macro
header = '?api-version=2018-10-18&Subscription-Key=' + API_KEY
url = 'https://api.wegmans.io/stores/'

def get_store(number):
    response = requests.get(url + str(number) + header)
    return response.json()

def get_stores():
    response = requests.get(url + header)
    return response.json()
