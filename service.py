# Some service functions and data
import sys
from currency import CURRENCIES, INFO_CURRENCIES, show_currencies

MESSAGE_FIRST_CURRENCY = 'Enter the first currency to convert (or the command): '
MESSAGE_CURRENCY_ERR = 'The selected currency does not exist! Try again'
MESSAGE_COMMAND_ERR = 'This user command does not exist! Try again'
MESSAGE_EXIT = 'Have a great day and see you again!'
EXIT_LIST = ['exit', 'quit', 'no']


def print_currency_error() -> None:
    """Prints message about wrong currency input"""
    print(MESSAGE_CURRENCY_ERR)


def print_command_error() -> None:
    """Prints message about wrong user command 'info'"""
    print(MESSAGE_COMMAND_ERR)


def check_currency_is_alpha(parameter: str) -> bool:
    """Checks parameter is valid alpha currency"""
    return parameter.isalpha() and parameter.upper() in CURRENCIES


def check_currency_is_digit(parameter: str) -> bool:
    """Checks parameter is valid digit currency"""
    if not parameter.isdigit():
        return False
    try:
        pos = int(parameter.lstrip('0'))
        if INFO_CURRENCIES.iloc[pos - 1]:
            return True
    except IndexError:
        return False


def handle_specific_command(prompt: str) -> None:
    """One word command processing"""
    if prompt.lower() == 'show':
        show_currencies()
        return

    if prompt.lower() in EXIT_LIST:
        print(MESSAGE_EXIT)
        sys.exit(0)
