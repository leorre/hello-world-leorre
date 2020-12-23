from flask import Flask,redirect, url_for, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def mainPage():
    return render_template('MainPage - Copy for Arsenis Part.html')


@app.route('/contactme')
def contactPage():
    return render_template('ContactMe.html')


@app.route('/amsagol')
def amSagolPage():
    return render_template('AmSagolVolunteering.html')


@app.route('/contactlist')
def contactListPage():
    return render_template('listUsersArseni.html')


@app.route('/assignment8')
def assignment8Page():
    return render_template('assignment8.html', hobby='Sleeping', user="Leorre", hobbies=['Long walks','Eating','Programming'])

if __name__ == '__main__':
    app.run(debug=True)
