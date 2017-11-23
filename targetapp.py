from flask import request, render_template
from flask_api import FlaskAPI, status
import json
from time import strftime, gmtime

app = FlaskAPI(__name__)


@app.route('/main')
def mainpage():
    return render_template('index-light.html')


@app.route('/stores')
def storepage():
    return render_template('stores.html')


@app.route('/customer/order')
def orderpage():
    return render_template('order.html')


@app.route('/customer/cart')
def cartpage():
    return render_template('cart.html')


@app.route('/signup')
def signuppage():
    return render_template('customer_sign_up.html')


@app.route('/signin')
def signinpage():
    return render_template('customer_Sign_in.html')


@app.route('/signup/success')
def successpage():
    return render_template('Signup_Success.html')


@app.route('/customer/account')
def accountpage():
    return render_template('payment.html')


if __name__ == "__main__":
    app.run()
