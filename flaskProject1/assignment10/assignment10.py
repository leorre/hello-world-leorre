from flask import Blueprint, render_template, request, session, redirect, Flask
import mysql.connector
import numpy as np


# assignment10 blueprint definition
assignment10 = Blueprint('assignment10',__name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


# DB connection
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='homework')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# routes
@assignment10.route('/assignment10')
def assignment10Page():
    query = "select * from users"
    queryResult = interact_db(query = query, query_type = 'fetch')
    print (queryResult)
    if request.method == 'GET':
        print('get')
    return render_template('assignment10.html', users = queryResult)


@assignment10.route('/allUsers', methods=['GET', 'POST'])
def users():
    query = "SELECT * FROM users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('/assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['userName']
        email = request.form['userEmail']
        user_id = request.form['userId']
        query = "INSERT INTO users(name,email,id) VALUES ('%s','%s','%s')" % (name, email, user_id)
        interact_db(query=query, query_type='commit')
    return users()


@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args['Id']
        query = "DELETE FROM users WHERE id='%s';" % (user_id)
        interact_db(query=query, query_type='commit')
    return users()


@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        if name != "": #update name
            query = "UPDATE users SET name='%s' WHERE id='%s'" %(name, id)
            interact_db(query, query_type='commit')
        if email != "":  # update email
            query = "UPDATE users SET email='%s' WHERE id='%s'" % (email, id)
            interact_db(query, query_type='commit')
    return users()