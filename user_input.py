# User input processing
import sys

from get_data_api import CURRENCIES
from currency import INFO_CURRENCIES, show_currencies

# Global variables for first and second currency and total amount
first_currency, amount, second_currency = [None] * 3
no_result = True

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
    return parameter.isdigit() #and parameter.lstrip('0') in CODES_CURRENCIES


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
            # elif amount is None:
            #     pass
                # check_user_amount(prompt)
            # print(first_currency)
        case 2:  # Info command from user
            process_info_command(prompt)


def check_currency(prompt: str) -> None:
    """Check currency input, support '006' format"""
    if check_currency_is_alpha(prompt):
        process_currency(prompt, True)
    else:
        try:
            if check_currency_is_digit(prompt):
                process_currency(prompt.lstrip('0'), False)
            else:
                print_currency_error()
        except ValueError:
            print_currency_error()


def process_currency(prompt: str, is_alpha: bool) -> None:
    """Process user input for existing currency"""
    global first_currency
    #first_currency = prompt.upper() if is_alpha else CODES_CURRENCIES.get(prompt)


# def check_user_amount(prompt: str) -> None:
#     print('OK')


def process_info_command(prompt: str) -> None:
    """Process for info command from user"""
    user_input = prompt.split()
    command, parameter = user_input[0], user_input[1]

    # Check conditions
    check_info = command.lower() == 'info'
    check_alpha = check_currency_is_alpha(parameter)
    check_digit = check_currency_is_digit(parameter)
    check_all = parameter.lower() == 'all'
    wrong_input = not check_info and (not check_alpha or not check_digit or not check_all)

    if wrong_input:                             # Wrong command input
        print_command_error()
        return

    if not check_all:
        if check_alpha:         # For alpha input info command
            print(f'{parameter.upper()} - {INFO_CURRENCIES.get(parameter.upper())}')
        elif check_digit:       # For digit input info command
            # currency_name = CODES_CURRENCIES.get(parameter.lstrip('0'))
            index = int(parameter.lstrip('0'))
            currency_name = INFO_CURRENCIES.iloc[index]
            print(f'{currency_name} - {INFO_CURRENCIES.get(currency_name)}')
