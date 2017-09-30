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
        user = request.form['username']
        password = request.form['password']

        cursor.execute('''SELECT password FROM User WHERE username = \"{}\"'''.format(user))
        if cursor.rowcount != 0:
            data = cursor.fetchall()[0][0]
            if data == password:
                return redirect(url_for('profile'))
            else:
                errors.append("Wrong password")
        return render_template('login.html', errors= errors)
    return render_template('login.html', errors= errors)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
