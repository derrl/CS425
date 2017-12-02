from flask import request, render_template, redirect
from flask_api import FlaskAPI, status, response
import json
from time import strftime, gmtime

app = FlaskAPI(__name__)


@app.route('/')
def redirect_to_main():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    return response

@app.route('/main')
def mainpage():
    if "auth_user" in request.cookies:
        return render_template('after_sign_in_indexpage.html')
    else:
        return render_template('index_light.html')

@app.route('/logout')
def logout():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    response.set_cookie('auth_user', value='', expires=0)  # Add the username arg
    return response

@app.route('/stores')
def storepage():
    return render_template('stores.html')


@app.route('/customer/order')
def orderpage():
    return render_template('order.html')


@app.route('/customer/cart')
def cartpage():
    return render_template('cart.html')




@app.route('/customer/signin', methods=['GET', 'POST'])
def signinpage():
    if request.method == 'GET':
        return render_template('customer_sign_in.html')
    if request.method == 'POST':
        # SIGN IN LOGIC
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        response.set_cookie('auth_user', value='')  # Add the username arg
        return response

@app.route('/signup')
def signuppage():
    return render_template('customer_sign_up.html')

@app.route('/signup/success')
def successpage():
    return render_template('signup_success.html')

@app.route('/test')
def test():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    response.set_cookie('auth_user', value='test')  # Add the username arg
    return response

@app.route('/customer/account')
def accountpage():
    return render_template('payment.html')


@app.route('/employee/signin', methods=['GET', 'PUT'])
def empSignin():
    if request.method == 'GET':
        return render_template('employee_sign_in.html')
    if request.method == 'POST':
        # SIGN IN LOGIC
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        response.set_cookie('auth_user', value='')  # Add the username arg
        response.set_cookie('employee', value='True')
        return response

@app.route('/employee/product')
def productCheck():
    if ("employee" in request.cookies) & (request.cookie["employee"] == "True"):
        return render_template("employee_check_product.html")
    else:
        return "FORBIDDEN"

@app.route('/employee/product/update')
def productUpdate():
    if ("employee" in request.cookies) & (request.cookie["employee"] == "True"):
        return render_template("update_productinfo.html")
    else:
        return "FORBIDDEN"





if __name__ == "__main__":
    app.run()
