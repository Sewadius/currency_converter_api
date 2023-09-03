# Handle with currency dictionary
from get_data_api import CURRENCIES
from json import loads

# Separator for currency output
OUTPUT_DIVIDER = 6

# Number codes dictionary for currencies
NUM_CURRENCIES = {}


def show_currencies() -> None:
    """Show information about all currencies"""
    print('\nThe following currencies are available:')
    for i, key in enumerate(CURRENCIES, start=1):
        print(f'{i}. {key}', end=' | ')
        if not i % OUTPUT_DIVIDER:
            print()
        # Filling in the dictionary with numerical codes
        NUM_CURRENCIES[i] = CURRENCIES[key]
    print()


def info_about_currencies():
    """Get information about currencies from file"""
    file_json = open('info.json', "r")
    return loads(file_json.read())


# Dictionary with information about currencies
INFO_CURRENCIES = info_about_currencies()
