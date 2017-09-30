from flask.ext.mysql import mysql

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'team1'
app.config['MYSQL_DATABASE_DB'] = 'cfg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

db = mysql.connect()
