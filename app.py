from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
cc = CurrencyCodes()
cr = CurrencyRates()
app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


CURRENCIES  = { 'IDR' : 'Indonesian rupiah', 'BGN' : 'Bulgarian lev', 'ILS' : 'Israeli new sheqel', 'GBP' : 'British pound', 'DKK' : 'Danish krone', 'CAD' : 'Canadian dollar', 'JPY' : 'Japanese yen', 'HUF' : 'Hungarian forint', 'RON' : 'Romanian leu', 'MYR' : 'Malaysian ringgit', 'SEK' : 'Swedish krona', 'SGD' : 'Singapore dollar', 'HKD' : 'Hong Kong dollar', 'AUD' : 'Australian dollar', 'CHF' : 'Swiss franc', 'KRW' : 'South Korean won', 'CNY' : 'Chinese/Yuan renminbi', 'TRY' : 'Turkish new lira', 'HRK' : 'Croatian kuna', 'NZD' : 'New Zealand dollar', 'THB' :  'Thai baht', 'EUR':  'European Euro', 'NOK' : 'Norwegian krone', 'RUB' : 'Russian ruble', 'INR' : 'Indian rupee', 'MXN' : 'Mexican peso', 'CZK' : 'Czech koruna', 'BRL' : 'Brazilian real', 'PLN' : 'Polish zloty','PHP' : 'Philippine peso', 'ZAR' : 'South African rand', 'USD' : 'United States dollar', 'BTC' : 'Bitcoin'}


@app.route("/")
def currency_converter():
    """Show currency converter form"""
    return render_template("currencyConverter.html", currencies = CURRENCIES)




@app.route("/converted", methods=["POST"])
def conversion():
    """Show amount conversion with a way back to the currency converter form"""
    convert_this = request.form['currency_type']
    converted = request.form['converted_currency']
    amount = request.form['amount']
    new_amount = cr.convert({convert_this, converted, amount})
    currency_symbol = cc.get_symbol({converted})

    return render_template("conversion.html", new_amount= new_amount, currency_symbol= currency_symbol)
