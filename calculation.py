from currency import INFO_CURRENCIES
from get_data_api import CURRENCIES


def calculate_result(first_cur, total, second_cur) -> None:
    """Returns value of the conversion"""
    result = round(CURRENCIES.get(second_cur) / CURRENCIES.get(first_cur) * total, 2)
    print_result(first_cur, second_cur, total, result)


def print_result(first_cur, second_cur, total, value) -> None:
    """Prints the final result"""
    input_currency = INFO_CURRENCIES.get(first_cur)
    converted_currency = INFO_CURRENCIES.get(second_cur)
    print(f'Result: {total} {input_currency} = {value} {converted_currency}')
