from flask import request, render_template, redirect
from flask_api import FlaskAPI, status, response
import cx_Oracle

app = FlaskAPI(__name__)
dsnstr = cx_Oracle.makedsn("fourier.cs.iit.edu", "1521", "orcl")
#connection = cx_Oracle.connect(user="hyang59", password="YOURORACLEPASSWORD", dsn=dsnstr)

@app.route('/')
def redirect_to_main():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    return response

@app.route('/main')
def mainpage():
    if "auth_user" in request.cookies:
        if "employee" in request.cookies:
            if request.cookies["employee"] == "True":
                return render_template('after_sign_in_indexpage_employee.html')
            else:
                return render_template('after_sign_in_indexpage_customer.html')
        else:
            return render_template('after_sign_in_indexpage_customer.html')
    else:
        return render_template('index_light.html')

@app.route('/logout')
def logout():
    redirect_to_main = redirect('/main')
    response = app.make_response(redirect_to_main)
    response.set_cookie('auth_user', value='', expires=0)  # Remove cookies
    response.set_cookie('employee', value='', expires=0)  # Remove cookies
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
        payload = request.get_json(force=True)
        userid = None
        cursor = connection.cursor()
        querystr = '''
            select user_id from account
            where username = {0}
            and password = {1};
        '''.format(payload["username"], payload["password"])
        cursor.execute(querystr)
        for id in cursor:
            userid = id
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        if not userid == None:
            response.set_cookie('auth_user', value=userid)  # Add the username arg
        return response

@app.route('/customer/signup', methods=['GET', 'POST'])
def signuppage():
    if request.method == "GET":
        return render_template('customer_sign_up.html')
    elif request.method == "POST":
        # SIGN UP LOGIC
        payload = request.get_json(force=True)
        cursor = connection.cursor()
        querystr = '''
        select username from account
        where username = {0};
        '''.format(payload["username"])
        cursor.execute(querystr)
        if len(cursor) != 0:
            return "USERNAME ALREADY EXISTS"
        cursor = connection.cursor()
        querystr = '''insert into customers
                values ({0},
                {1},
                {2},
                {3},
                {4},
                {5},
            );        
        '''.format(payload["userid"], payload["firstname"], payload["middlename"],
                   payload["lastname"], payload["phoneno"], payload["dateofbirth"])
        cursor.execute(querystr)
        redirect_to = redirect('customer/signup/success')
        response = app.make_response(redirect_to)
        return response
@app.route('/customer/signup/success')
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
    return render_template('update_customerinfo.html')

@app.route('/customer/account/update', methods=['GET', 'POST'])
def accountUpdate():
    if request.method == 'POST':
        # UPDATE LOGIC
        payload = request.get_json(force=True)
        cursor = connection.cursor()
        querystr = '''
                select username from account
                where username = {0};
                '''.format(payload["username"])
        cursor.execute(querystr)
        cursor = connection.cursor()
        querystr = '''insert into customers
                        values ({0},
                        {1},
                        {2},
                        {3},
                        {4},
                        {5},
                    );        
                '''.format(payload["userid"], payload["firstname"], payload["middlename"],
                           payload["lastname"], payload["phoneno"], payload["dateofbirth"])
        cursor.execute(querystr)
        redirect_to_main = redirect('/main')
        response = app.make_response(redirect_to_main)
        return response

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
