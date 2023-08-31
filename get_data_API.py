from get_key_API import HOST
import requests


def get_api_currencies() -> dict:
    response = requests.get(HOST)
    return response.json().get('data')


CURRENCIES = get_api_currencies()
