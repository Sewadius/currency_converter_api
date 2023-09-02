# Handle with currency dictionary
from get_data_api import CURRENCIES

OUTPUT_DIVIDER = 6
INFO_CURRENCIES = {
    'AUD': 'Australian dollar',
    'BGD': 'Bulgarian lev',
    'BRL': 'Brazilian real'
}

def show_currencies() -> None:
    """Show information about all currencies"""
    print('\nThe following currencies are available:')
    for i, key in enumerate(CURRENCIES, start=1):
        print(f'{i}. {key}', end=' | ')
        if not i % OUTPUT_DIVIDER:
            print()
    add_info_about_currencies()
    print(f'\n{CURRENCIES}')

def add_info_about_currencies():
    pass
