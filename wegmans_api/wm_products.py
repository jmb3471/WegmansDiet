"""
Wegmans Products API Wrapper
Written at Brickhack 2020
author: Joshua Yoder <jpfyoder>
author: Dhaval Shrishrimal
"""

# external packages
import requests

# import authorization key from auth.py, hidden from git
from wegmans_api.auth import API_KEY
from wegmans_api.check_status import check_status

# authorization header and url macro
header = '?api-version=2018-10-18&Subscription-Key=' + API_KEY
url = 'https://api.wegmans.io/products/'


def get_location(sku, store):
    response = requests.get(url + str(sku) + '/locations/' + str(store) + header)
    check_status(response)
    return response.json()


def get_locations(sku):
    response = requests.get(url + str(sku) + '/locations' + header)
    check_status(response)
    return response.json()


def search_products(p_name):
    text = "search?query=" + p_name + "&"
    response = requests.get(url + text + header[1:])
    check_status(response)
    return response.json()


def get_prices(sku):
    response = requests.get(url + str(sku) + '/prices' + header)
    check_status(response)
    return response.json()


def get_categories():
    response = requests.get(url + 'categories' + header)
    check_status(response)
    return response.json()


def get_category(category):
    response = requests.get(url + 'categories/' + str(category) + header)
    check_status(response)
    return response.json()


def get_product(sku):
    response = requests.get(url + str(sku) + header)
    check_status(response)
    return response.json()


def get_products():
    response = requests.get(url + header)
    check_status(response)
    return response.json()


def get_price(sku, store):
    response = requests.get(url + str(sku) + '/prices/' + str(store) + header)
    check_status(response)
    return response.json()


def get_availabilities(sku):
    response = requests.get(url + str(sku) + '/availabilities' + header)
    check_status(response)
    return response.json()


def get_availability(sku, store):
    response = requests.get(url + str(sku) + '/availabilities/' + str(store))
    check_status(response)
    return response.json()


