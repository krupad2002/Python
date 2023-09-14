import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to insert form data into the MySQL database


def insert_form_data(name, email, message, gender, subscribe):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password', 
        database='form_data'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO  users (name, email, message, gender, subscribe) VALUES (%s, %s, %s, %s, %s)'
    if subscribe == 'on':
        subscribe = 1
    else:
        subscribe = 0
    data = (name, email, message, gender, subscribe)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['mail']
        message = request.form['message']
        gender = request.form['gender']
        subscribe = request.form.get('Subscribe', False)

        insert_form_data(name, email, message, gender, subscribe)

        return 'Form submitted successfully!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
