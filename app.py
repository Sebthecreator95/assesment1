from os import error
from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forms import ConvertForm
from common import check_code, CURRENCIES
cc = CurrencyCodes()
cr = CurrencyRates()
app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config
app.debug = True
debug = DebugToolbarExtension(app)



@app.route("/", methods=["GET","POST"])
def currency_converter():
    """Show currency converter form"""
    form =ConvertForm()
    if form.validate_on_submit():
        try:
            converting_currency = check_code(form.converting_from.data.upper())
            converted_currency = check_code(form.converting_to.data.upper())
            currency_code = cc.get_symbol(converted_currency)
            amount = form.amount.data
            new_amount = cr.convert(converting_currency, converted_currency, amount)
            flash('congratulations, you have made a conversion! p.s. currency rates change make sure you get your latest rate', 'success')
            return render_template("conversion.html", new_amount= new_amount, currency_code= currency_code)
        except (Exception, AttributeError) as errs:
            flash('Invalid conversion or API down', 'err')
            flash(f'{errs}','err')
            return redirect('/')
   

    return render_template("currencyConverter.html", currencies = CURRENCIES, form=form)
