from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates

app = Flask(__name__)


@app.route("/display_forex_form")
def display_forex_form():
    """Show mypage, an example of template inheritance"""

    return render_template("form.html")

@app.route("/get_results", methods = ['POST'])
def display_results():
    curr_rates = CurrencyRates()
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]
    amount = float(request.form["amount_to_convert"])
    #converted_amount = curr_rates.convert(from_currency,to_currency,amount)

    converted_amount = amount * 2; # for now
    print(converted_amount)


    return render_template("results.html", converted_amount=converted_amount)
