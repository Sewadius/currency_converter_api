# Obtaining API Key from JSON file
from json import loads


def get_api_key() -> str:
    """Get API Key from JSON file"""
    file_json = open('json/key.json', "r")
    data = loads(file_json.read())
    return data['key']


API_KEY = get_api_key()
HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
