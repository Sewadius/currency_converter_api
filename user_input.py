# User input processing
from get_data_api import CURRENCIES
from currency import NUM_CURRENCIES, show_currencies

MESSAGE_FIRST_CURRENCY = 'Enter the first currency to convert or the command: '
MESSAGE_AMOUNT = 'Enter the desired amount: '

MESSAGE_CURRENCY_ERR = 'The selected currency does not exist! Try again'

# Global variables for first and second currency and total amount
first_currency, amount, second_currency = [None] * 3
no_result = True


def print_currency_error() -> None:
    print(MESSAGE_CURRENCY_ERR)


def get_user_command() -> None:
    """Get command from user"""
    while first_currency is None:
        user_prompt = input(MESSAGE_FIRST_CURRENCY)
        handle_user_input(user_prompt)
    while amount is None:
        user_amount = input(MESSAGE_AMOUNT)
        handle_user_input(user_amount)


def handle_user_input(prompt: str) -> None:
    """Selection depending on the length of the command"""
    length = len(prompt.split())
    match length:
        case 1:  # Code or number for currency
            if first_currency is None:
                process_first_currency(prompt)
            elif amount is None:
                process_user_amount(prompt)
            # print(first_currency)
        case 2:  # Info command from user
            process_info_command(prompt)


def process_first_currency(prompt: str) -> None:
    """Process user input for first currency"""
    if prompt.lower() == 'show':
        show_currencies()
        return

    global first_currency
    check_alpha = all([prompt.isalpha(), prompt.upper() in CURRENCIES])
    check_digit = False
    if not check_alpha:
        try:
            check_digit = all([prompt.isdigit(), int(prompt) in NUM_CURRENCIES])
        except ValueError:
            print_currency_error()
            return

    if check_alpha:                   # For string code input
        first_currency = prompt.upper()
    if check_digit:                   # For digit code input
        first_currency = int(prompt)
    if first_currency is None:        # Error input
        print_currency_error()


def process_user_amount(prompt: str) -> None:
    print('OK')


def process_info_command(prompt: str) -> None:
    pass
