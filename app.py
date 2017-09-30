from flask import *
from flask.ext.mysql import MySQL

import controllers
app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cfg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

db = mysql.connect()
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    errors = []
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute('''SELECT password FROM User WHERE username = \"{}\"'''.format(username))
        if cursor.rowcount != 0:
            data = cursor.fetchall()[0][0]
            if data == password:
                cursor.execute('''SELECT bio FROM User WHERE username = \"{}\"'''.format(username))
                bio = cursor.fetchall()[0][0]

                cursor.execute('''SELECT journeyid FROM UserJourney WHERE username = \"{}\"'''.format(username))
                userjournies = cursor.fetchall()

                # Turn tuple of single-tuple items into list
                userjournies = [x[0] for x in data] 
                return redirect(url_for('profile_route', username=username,
                                                   userjournies=userjournies,
                                                   bio=bio))
            else:
                errors.append("Wrong password")
        return render_template('login.html', errors= errors)
    return render_template('login.html', errors= errors)

@app.route('/profile', methods=['GET', 'POST'])
def profile_route():
     username = request.args.get('username')
     raise
#    cursor.execute('''SELECT bio FROM User WHERE username = \"{}\"'''.format(username))
#    cursor.execute('''SELECT bio FROM User WHERE username = \"{}\"'''.format(username))
#    cursor.execute('''SELECT bio FROM User WHERE username = \"{}\"'''.format(username))


@app.route('/journey', methods=['GET', 'POST'])
def journey_route():
    journey_selected = request.args.get('journey_selected')
    
    cursor.execute('''SELECT * FROM Journey''')
    data = cursor.fetchall()
    journies = {x[1]:x[0] for x in data}

    stuff = []
    for i in journies.values():
        cursor.execute('''SELECT reactiondata FROM Reactions WHERE journeyid = {}'''.format(i))
        data = cursor.fetchall()
        stuff.append(data)
        #raise

    raise

    if journey_selected == None:
        return render_template('journey.html', journey_selected=None, journies=data)
    else:
        journies = request.args.get('journies')
        reactions = request.args.get('reactions')

    

@app.route('/class')
def class_route():
    gradyear = request.args.get('gradyear')
    if gradyear == None:
        cursor.execute('''SELECT MAX(gradyear) FROM Class''')
        #gradyear = 
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
