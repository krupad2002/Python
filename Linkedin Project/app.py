import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to insert form data into the MySQL database

def signup_data(mobileoremail, password, conf_password):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password', 
        database='linkedin'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO signup (mobileoremail, password, conf_password) VALUES (%s, %s, %s)'
    data = (mobileoremail, password, conf_password)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

def login_data(mobileoremail, password):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password', 
        database='linkedin'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO login (mobileoremail, password) VALUES (%s, %s)'
    data = (mobileoremail, password)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

def account_details_data(name, gender, university, degree, address):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='linkedin'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO accountdetails (name, gender, university, degree, address) VALUES (%s,%s,%s,%s,%s)'
    data = (name, gender, university, degree, address)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mobileoremail=request.form['mobileoremail']
        password=request.form['password']
        conf_password=request.form['conf_password']

        signup_data(mobileoremail,password,conf_password)

        return render_template('login.html')
    
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mobileoremail=request.form['mobileoremail']
        password=request.form['password']

        login_data(mobileoremail,password)

        return render_template('home.html')

    return render_template('login.html')

@app.route('/accdetail', methods=['GET', 'POST'])
def acc_details():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        university = request.form['university']
        degree = request.form['degree']
        address = request.form['address']
    
        account_details_data(name, gender, university, degree,address)
        return 'added sucessfully'
    return render_template('account_details.html')

if __name__ == '__main__':
    app.run(debug=True)
