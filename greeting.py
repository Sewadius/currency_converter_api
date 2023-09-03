# Welcome and info for user
def greets() -> None:
    """Welcome and info for user about the programme"""
    print("""Welcome to our currency converter!
    
Our programme allows you to convert currencies:
1. Select your currency
2. Enter the amount of this currency
3. Select the currency to convert

You can request information about an individual currency or all of them
Just use command "info AUD" or "info 1" for example and "info all\"
You can also convert currencies in one line like "USD 11.55 EUR\"
There is a "show" command that shows the list of currencies again""")
