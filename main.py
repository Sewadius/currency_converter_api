#!/usr/bin/python3
from greeting import greets
from currency import show_currencies
from user_input import get_user_command


def main() -> None:
    """Main function for program"""
    greets()                # Greeting for user
    show_currencies()       # Show info about currencies
    get_user_command()      # Command for user


if __name__ == '__main__':
    main()
