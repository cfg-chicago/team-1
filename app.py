from flask import *
#from flask.ext.mysql import MySQL
app = Flask(__name__)
'''
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'team1'
app.config['MYSQL_DATABASE_DB'] = 'cfg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

db = mysql.connect()
cursor = db.cursor()
'''
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=4000, debug=True)
