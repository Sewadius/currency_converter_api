import sys

from requests.exceptions import RequestException
from requests import get
from get_key_api import HOST


def get_api_currencies() -> dict:
    """Retrieving currency data via query"""
    response = get(HOST)
    return response.json().get('data')


# Handling exceptions when there is no internet connection
try:
    CURRENCIES = get_api_currencies()
except RequestException:
    print('Server communication error, check internet connection')
    sys.exit(0)
