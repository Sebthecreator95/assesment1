CURRENCIES  = { 'IDR' : 'Indonesian rupiah', 'BGN' : 'Bulgarian lev', 'ILS' : 'Israeli new sheqel', 'GBP' : 'British pound', 'DKK' : 'Danish krone', 'CAD' : 'Canadian dollar', 'JPY' : 'Japanese yen', 'HUF' : 'Hungarian forint', 'RON' : 'Romanian leu', 'MYR' : 'Malaysian ringgit', 'SEK' : 'Swedish krona', 'SGD' : 'Singapore dollar', 'HKD' : 'Hong Kong dollar', 'AUD' : 'Australian dollar', 'CHF' : 'Swiss franc', 'KRW' : 'South Korean won', 'CNY' : 'Chinese/Yuan renminbi', 'TRY' : 'Turkish new lira', 'HRK' : 'Croatian kuna', 'NZD' : 'New Zealand dollar', 'THB' :  'Thai baht', 'EUR':  'European Euro', 'NOK' : 'Norwegian krone', 'RUB' : 'Russian ruble', 'INR' : 'Indian rupee', 'MXN' : 'Mexican peso', 'CZK' : 'Czech koruna', 'BRL' : 'Brazilian real', 'PLN' : 'Polish zloty','PHP' : 'Philippine peso', 'ZAR' : 'South African rand', 'USD' : 'United States dollar'}


def check_code(code):
    if code in CURRENCIES:
        return code
    raise AttributeError(f'Invalid Currency Code {code}  Or It Does Not Exist')



def check_amount(amount):
    if (isinstance(amount, int)) or (isinstance(amount, float)):
        if amount == 0:
            raise Exception('can not convert 0')
        return amount
    raise TypeError('Not A Valid Amount')
