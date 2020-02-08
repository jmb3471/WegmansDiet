"""
Wegmans Products API Wrapper
Written at Brickhack 2020
author: Joshua Yoder <jpfyoder>
author: Dhaval Shrishrimal
"""

# external packages
import requests
import json

# import authorization key from auth.py, hidden from git
from auth import API_KEY

# authorization header and url macro
header = '?api-version=2018-10-18&Subscription-Key=' + API_KEY
url = 'https://api.wegmans.io/products/'


def get_location(sku, store):
    response = requests.get(url + str(sku) + '/locations/' + str(store) + header)
    return response.json()


def get_locations(sku):
    response = requests.get(url + str(sku) + '/locations' + header)
    return response.json()


def search_products():
    p_name = input("Enter product name: ")
    text = "search?query=" + p_name + "&"
    result = requests.get(url + text + header[1:])
    return result.json()


def get_prices(sku):
    response = requests.get(url + str(sku) + '/prices' + header)
    return response.json()


def get_categories():
    response = requests.get(url + 'categories' + header)
    return response.json()


def get_category(category):
    response = requests.get(url + 'categories/' + str(category) + header)
    return response.json()


def get_product(sku):
    response = requests.get(url + str(sku) + header)
    return response.json()


def get_products():
    response = requests.get(url + header)
    return response.json()


def get_price(sku, store):
    response = requests.get(url + str(sku) + '/prices/' + str(store) + header)
    return response.json()


def get_availabilities(sku):
    response = requests.get(url + str(sku) + '/availabilities' + header)
    return response.json()


def get_availability(sku, store):
    response = requests.get(url + str(sku) + '/availabilities/' + str(store))
    return response.json()


