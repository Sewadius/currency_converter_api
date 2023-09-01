
from greeting import greets
from currency import show_currencies


# MESSAGE_CURRENCY_ERROR = 'Выбранной валюты нет! Попробуйте снова.'
# MESSAGE_AMOUNT_ERROR = 'Неверно введена сумма! Попробуйте снова.'

# def print_currencies():
#     print("Имеются следующие валюты:")
#     i = 1
#     for key, value in CURRENCIES.items():
#         print(f"{i}. {key}")
#         i += 1
#
# def input_current_currency():
#     while True:
#         current_currency = input("Введите свою валюту: ").upper()
#         if current_currency in CURRENCIES.keys():
#             break
#         # Интересный подход
#         print(MESSAGE_CURRENCY_ERROR)
#     return current_currency
#
# # Название аргумента s мало информативно
# def is_float(s: str) -> bool:
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
#
# def input_amount():
#     while True:
#         amount = input("Введите сумму: ")
#         if is_float(amount) and float(amount) > 0:
#             amount = float(amount)
#             break
#         print(MESSAGE_AMOUNT_ERROR)
#     return amount
#
# def input_converting_currency():
#     while True:
#         converting_currency = input("Выберите валюту для конвертации: ").upper()
#         if converting_currency in CURRENCIES.keys():
#             break
#         print(MESSAGE_CURRENCY_ERROR)
#     return converting_currency

# def get_print_result(conv_currency, cur_currency, amount):
#     converted_amount = CURRENCIES.get(conv_currency, 1) / CURRENCIES.get(cur_currency, 1) * amount
#     print(f"ИТОГО: {round(converted_amount, 2)} {converting_currency}")

if __name__ == '__main__':
    greets()                    # Greeting for user
    show_currencies()           # Show info about currencies
    # greeting()
    # print_currencies()
    #
    # while True:
    #     current_currency = input_current_currency()
    #     amount = input_amount()
    #     converting_currency = input_converting_currency()
    #     get_print_result(converting_currency, current_currency, amount)
    #
    #     user = input('Хотите запустить заново? (Да/Нет) ')
    #     if user.lower() == 'нет':
    #         break

