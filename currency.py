# Handle with currency dictionary
from get_data_api import CURRENCIES
from json import loads
import pandas as pd

# Separator for currency output by lines
OUTPUT_DIVIDER = 6


def show_currencies() -> None:
    """Show information about all currencies"""
    print('\nThe following currencies are available:')
    for i, key in enumerate(CURRENCIES, start=1):
        print(f'{i}. {key}', end=' | ')
        if not i % OUTPUT_DIVIDER:
            print()
    print('\n')


def read_info_about_currencies():
    """Get information about currencies from file"""
    file_json = open('json/info.json', "r")
    return loads(file_json.read())


# Pandas series with information about currencies
INFO_CURRENCIES = pd.Series(read_info_about_currencies())
