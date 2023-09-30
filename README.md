## Currency Converter API

<img src="img/currencies.jpg" style="height:200px">

*Ready*:
- get API key from .json file
- well-formatted currencies output
- print info about command "info" for currencies
- handle with Internet connection exceptions
- get info from user about the first currency
- remove `CODES_CURRENCIES` and using `pandas` module instead    

*Want to do*:
- last values saving to file .json from last Internet data
- get currencies from file there is no connection to Internet
- conversion in one line as `usd rub 11,15`
- write handle function for second currency input

*New*:  
- added module `service.py` for some functions and data  
- input for `amount` is ready with `,` replace and check negative  
- finished work with step-by-step input from user  
- using `calculation.py` for converting and getting the result  

*Fixes*:
- removed error message for `show` command  
- `info all` and `info` command are implemented  
