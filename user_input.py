# User input processing
import sys

from get_data_api import CURRENCIES
from currency import INFO_CURRENCIES, CODES_CURRENCIES, show_currencies

# Global variables for first and second currency and total amount
first_currency, amount, second_currency = [None] * 3
no_result = True

MESSAGE_FIRST_CURRENCY = 'Enter the first currency to convert (or the command): '
MESSAGE_CURRENCY_ERR = 'The selected currency does not exist! Try again'

MESSAGE_EXIT = 'Have a great day and see you again!'
EXIT_LIST = ['exit', 'quit', 'no']


def print_currency_error() -> None:
    print(MESSAGE_CURRENCY_ERR)


def handle_specific_command(prompt: str) -> None:
    """One word command processing"""
    if prompt.lower() == 'show':
        show_currencies()
        return

    if prompt.lower() in EXIT_LIST:
        print(MESSAGE_EXIT)
        sys.exit(0)


def get_user_command() -> None:
    """Get command from user"""
    while first_currency is None:
        user_prompt = input(MESSAGE_FIRST_CURRENCY)
        handle_user_input(user_prompt)
    while amount is None:
        info = INFO_CURRENCIES.get(first_currency)
        message_amount = f'Enter the desired amount of {first_currency} [{info}] (or the command): '
        user_amount = input(message_amount)
        handle_user_input(user_amount)


def handle_user_input(prompt: str) -> None:
    """Selection depending on the length of the command"""
    length = len(prompt.split())
    match length:
        case 1:  # Code or number for currency
            handle_specific_command(prompt)
            if first_currency is None:
                check_currency(prompt)
            elif amount is None:
                check_user_amount(prompt)
            # print(first_currency)
        case 2:  # Info command from user
            process_info_command(prompt)


def check_currency(prompt: str) -> None:
    """Check currency input, support '006' format"""
    if prompt.isalpha() and prompt.upper() in CURRENCIES:
        process_currency(prompt, True)
    else:
        try:
            if prompt.isdigit() and prompt.lstrip('0') in CODES_CURRENCIES:
                process_currency(prompt.lstrip('0'), False)
            else:
                print_currency_error()
        except ValueError:
            print_currency_error()


def process_currency(prompt: str, is_alpha: bool) -> None:
    """Process user input for existing currency"""
    global first_currency
    first_currency = prompt.upper() if is_alpha else CODES_CURRENCIES.get(prompt)


def check_user_amount(prompt: str) -> None:
    print('OK')


def process_info_command(prompt: str) -> None:
    pass
