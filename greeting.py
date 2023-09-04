# Welcome and info for user
def greets() -> None:
    """Welcome and info for user about the programme"""
    print("""Welcome to the currency converter!
    
Our programme allows you to convert currencies:
1. Select your first currency
2. Enter the amount of this currency
3. Select the second currency to convert

You can request information about an individual currency or all of them
Just use command "info AUD" or "info 1" for example and "info all\"
You can also convert currencies in one line like "usd eur 11,55\"
There is a "show" command that shows the list of currencies again
For exit, type "no", "exit" or "quit" as a command""")
