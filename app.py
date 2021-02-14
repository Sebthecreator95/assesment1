from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
cc = CurrencyCodes()
cr = CurrencyRates(force_decimal=False)
app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config
app.debug = True
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
    currency_symbol = cc.get_symbol(converted)
    if "-" in amount:
        flash('No Negative (-) Numbers Please', 'error')
        return redirect('/')
    if amount == "":
        flash('Please Submit A NUMBER', 'error')
        return redirect('/')
    if amount == 0:
        flash('Please Submit A NUMBER', 'error')
        return redirect('/')
    if (float(int(amount))).is_integer:
        if convert_this == 'BTC':
            if converted == 'BTC':
                new_amount = int(amount)
                currency_symbol = b.get_symbol()
                return render_template("conversion.html", new_amount= new_amount, currency_symbol= currency_symbol)
            else:
                new_amount = b.convert_btc_to_cur(int(amount), converted) 
                return render_template("conversion.html", new_amount= new_amount, currency_symbol= currency_symbol)
        elif converted == 'BTC':
            new_amount = b.convert_to_btc(int(amount), convert_this)
            currency_symbol = b.get_symbol()
            return render_template("conversion.html", new_amount= new_amount, currency_symbol= currency_symbol)
        else:
            new_amount = cr.convert(convert_this, converted, int(amount))
            flash('congratulations, you have made a conversion! p.s. currency rates change make sure you get your latest rate', 'success')
            return render_template("conversion.html", new_amount= new_amount, currency_symbol= currency_symbol)
    else:
        flash('Not A VALID NUMBER!!!', 'error')
        return redirect('/')
