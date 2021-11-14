from flask import Flask, redirect, flash


CURRENCIES  = { 'IDR' : 'Indonesian rupiah', 'BGN' : 'Bulgarian lev', 'ILS' : 'Israeli new sheqel', 'GBP' : 'British pound', 'DKK' : 'Danish krone', 'CAD' : 'Canadian dollar', 'JPY' : 'Japanese yen', 'HUF' : 'Hungarian forint', 'RON' : 'Romanian leu', 'MYR' : 'Malaysian ringgit', 'SEK' : 'Swedish krona', 'SGD' : 'Singapore dollar', 'HKD' : 'Hong Kong dollar', 'AUD' : 'Australian dollar', 'CHF' : 'Swiss franc', 'KRW' : 'South Korean won', 'CNY' : 'Chinese/Yuan renminbi', 'TRY' : 'Turkish new lira', 'HRK' : 'Croatian kuna', 'NZD' : 'New Zealand dollar', 'THB' :  'Thai baht', 'EUR':  'European Euro', 'NOK' : 'Norwegian krone', 'RUB' : 'Russian ruble', 'INR' : 'Indian rupee', 'MXN' : 'Mexican peso', 'CZK' : 'Czech koruna', 'BRL' : 'Brazilian real', 'PLN' : 'Polish zloty','PHP' : 'Philippine peso', 'ZAR' : 'South African rand', 'USD' : 'United States dollar'}


def check_code(code):
    if code in CURRENCIES:
        return code
    raise AttributeError(f'Invalid Currency Code {code}  Or It Does Not Exist')

def check_amount(amount):
    if amount == 0 or 0.00:
        raise ValueError('can not convert 0')
    return amount

def handle_errors(err, converted_currency, converting_currency):
    if (f'{err}' == f'Currency https://theforexapi.com/api/latest => {converted_currency} rate not available for Date latest.'):
        flash(f'Invalid currency : can not convert to {converted_currency}','err')
        return redirect('/')

    if (f'{err}' == 'Currency Rates Source Not Ready'):
        flash(f'Invalid currency : can not convert from {converting_currency}','err')
        return redirect('/')            

    if (f'{err}' == 'convert requires amount parameter is of type Decimal when force_decimal=True'):
        flash('Invalid Amount','err')
        return redirect('/') 
