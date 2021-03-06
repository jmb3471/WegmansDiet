"""
Wegmans Products API error checker
Written at Brickhack 2020
author: Joshua Yoder <jpfyoder>
author: Dhaval Shrishrimal
"""
import requests


def check_status(response):
    if response.status_code == 200:
        return
    elif response.status_code == 459:
        raise Exception("Too Many Requests! ")
    else:
        raise Exception("Status Code:" + str(response.status_code))
