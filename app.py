from flask import Flask, request, render_template
from datetime import datetime
from forex_python.converter import CurrencyRates, CurrencyCodes

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

    print(f"from_currency = {from_currency}")
    print(f"to_currency = {to_currency}")
    print(f"amount_currency = {amount}")

    ccodes = CurrencyCodes()
    ccode_display = ccodes.get_symbol(to_currency)
    #converted_amount = amount * 2; # for now
    #curr_rates.get_rate(from_currency, to_currency)
    # this has not been working... so try it with a date/time:
    date_obj =  datetime(2020, 5, 17) #arbitrary time in the past
    print(f"Date chosen: {date_obj.month}/{date_obj.day}/{date_obj.year}")
    try:
        converted_amount = curr_rates.convert(from_currency,to_currency,amount, date_obj)
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)
        converted_amount = 0.0;
    #print(converted_amount)


    return render_template("results.html", code=ccode_display, converted_amount=converted_amount)

