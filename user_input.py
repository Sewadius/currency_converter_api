# User input processing
from currency import INFO_CURRENCIES
import service as sv

# Global variables for first and second currency and total amount
first_currency, amount, second_currency = [None] * 3
no_result = True


def get_user_command() -> None:
    """Get command from user"""
    while first_currency is None:
        user_prompt = input(sv.MESSAGE_FIRST_CURRENCY)
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
            sv.handle_specific_command(prompt)
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
    if prompt.lower() == 'show':
        return
    if sv.check_currency_is_alpha(prompt):
        process_currency(prompt, True)
    else:
        try:
            if sv.check_currency_is_digit(prompt):
                process_currency(prompt.lstrip('0'), False)
            else:
                sv.print_currency_error()
        except ValueError:
            sv.print_currency_error()


def process_currency(prompt: str, is_alpha: bool) -> None:
    """Process user input for existing currency"""
    global first_currency

    if is_alpha:
        first_currency = prompt.upper()
    else:
        pos = int(prompt)
        first_currency = INFO_CURRENCIES.index[pos - 1]


# def check_user_amount(prompt: str) -> None:
#     print('OK')


def process_info_command(prompt: str) -> None:
    """Process for info command from user"""
    cmd, parameter = prompt.split()

    # Check conditions
    is_info = cmd.lower() == 'info'
    is_alpha = sv.check_currency_is_alpha(parameter)
    is_digit = sv.check_currency_is_digit(parameter)
    is_all = parameter.lower() == 'all'

    checks = [is_alpha, is_digit, is_all]
    wrong_input = not (is_info and any(checks))

    if wrong_input:
        sv.print_command_error()
        return

    handle_info_command(checks, parameter)


def handle_info_command(checks: list, par: str) -> None:
    """Handle for info command from user"""
    alpha, digit, all_check = checks

    if not all_check:   # Not all info command
        if alpha:       # For alpha input info command
            print(f'{par.upper()} - {INFO_CURRENCIES.get(par.upper())}')
        elif digit:     # For digit input info command
            pos = int(par.lstrip('0'))
            cur_name, cur_info = (
                INFO_CURRENCIES.index[pos - 1], INFO_CURRENCIES.iloc[pos - 1])
            print(f'{cur_name} - {cur_info}')
    else:               # Info all command
        for k, v in INFO_CURRENCIES.items():
            print(f'{k}: {v}')
        print()
