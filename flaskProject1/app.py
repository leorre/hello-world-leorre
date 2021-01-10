from flask import Flask, redirect, url_for, render_template, request, session
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
# app.config.from_pyfile('bla.py')

@app.route('/home')
@app.route('/')
def mainPage():
    return render_template('MainPage - Copy for Arsenis Part.html')


@app.route('/contactme')
def contactPage():
    return render_template('ContactMe.html')



@app.route('/amSagol')
def amSagolPage():
    return render_template('AmSagolVolunteering.html')



@app.route('/contactlist')
def contactListPage():
    return render_template('listUsersArseni.html')


@app.route('/assignment8')
def assignment8Page():
    return render_template('assignment8.html', hobby='Sleeping', user="Leorre", hobbies=['Long walks', 'Eating', 'Programming'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9Page():
    username = ''
    foundName = 0
    users = [('Lee', 'lee@gmail.com'),
           ('Naama', 'naama@gmail.com'),
           ('Evyatar', 'evyatar@gmail.com'),
           ('Arseni', 'arseni@gmail.com'),
           ('Limor', 'limor@gmail.com'),
           ('Moshe', 'moshe@gmail.com')]
    if request.method == 'GET':
        if 'firstName' in request.args:
            foundName = 1
            name = request.args['firstName']
            return render_template('assignment9.html', request_method=request.method, foundName=foundName,
                                   name=name, users=users)
    if request.method == 'POST':
        username = request.form.get('username', False)
        session['username'] = username
        session['login'] = True
        return render_template('assignment9.html', request_method=request.method, foundName=foundName,
                               username=username, users=users)
    return render_template('assignment9.html',request_method=request.method, foundName=foundName, users=users)


@app.route('/logout')
def logoutPage():
    session['login'] = False
    return render_template('assignment9.html')


# blueprint assignment 10
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


if __name__ == '__main__':
    app.secret_key = '123'
    app.run(debug=True)
