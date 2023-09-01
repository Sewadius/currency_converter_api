# Handle with currency dictionary
from get_data_api import CURRENCIES

OUTPUT_DIVIDER = 6


def show_currencies() -> None:
    """Show information about all currencies"""
    print('\nThe following currencies are available:')
    for i, key in enumerate(CURRENCIES, start=1):
        print(f'{i}. {key}', end=' | ')
        if not i % OUTPUT_DIVIDER:
            print()
