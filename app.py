from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forms import ConvertForm
from common import check_code, CURRENCIES, handle_errors, check_amount
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
            amount = str(check_amount(form.amount.data))
            return redirect(f'/converted/{converting_currency}/{converted_currency}/{amount}')
        except AttributeError as err:
            flash(f'{err}','err')
            return redirect('/')
        except (ValueError, TypeError) as err:
            flash(f'{err}','err')
            return redirect('/')


    return render_template("currencyConverter.html", currencies = CURRENCIES, form=form)

@app.route("/converted/<string:converting>/<string:converted>/<string:amount>", methods=["GET"])
def conversion(converting, converted, amount):
    """Money converted"""
    try:
        new_amount = round(cr.convert(converting, converted, float(amount)),2)
    except Exception as err:
            handle_errors(err, converted, converting)
            flash('Invalid conversion or API down', 'err')
            flash(f'{err}','err')
            return redirect('/')
    flash('congratulations, you have made a conversion! p.s. currency rates change make sure you get your latest rate', 'success')
    return render_template("conversion.html", new_amount= new_amount, currency_code = cc.get_symbol(converted))