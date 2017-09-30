from flask import Flask, render_template, request, redirect, url_for, session
import extensions
import config

app = Flask(__name__, template_folder='templates')
db = extensions.connect_to_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
	errors = []
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		cursor = db.cursor()
		cursor.execute('''SELECT password FROM User WHERE username = \"{}\"'''.format(username))
		if cursor.rowcount != 0:
			data = cursor.fetchall()[0]
			if data['password'] == password:
				cursor.execute('''SELECT bio FROM User WHERE username = \"{}\"'''.format(username))
				bio = cursor.fetchall()[0]['bio']

				cursor.execute('''SELECT journeyid FROM UserJourney WHERE username = \"{}\"'''.format(username))
				userjournies = cursor.fetchall()

				# Turn tuple of single-tuple items into list
				userjournies = [x['journeyid'] for x in userjournies] 
				session['username'] = username
				return redirect(url_for('profile_route', username=username,
													userjournies=userjournies,
													bio=bio))
			else:
				errors.append("Wrong password")
		return render_template('login.html', errors= errors)
	return render_template('login.html', errors= errors)

@app.route('/logout', methods=['GET', 'POST'])
def logout_route():
	session.pop(username)
	return redirect(url_for('login_route'))

@app.route('/profile', methods=['GET', 'POST'])
def profile_route():
	username = request.args.get('username')
	bio = request.args.get('bio')
	userjournies = request.args.getlist('userjournies')
	journies = []
	reflections = {}
	for x in userjournies:
		cur = db.cursor()
		cur.execute("SELECT * FROM Journey WHERE journeyid = (%s)", (x))
		journey = cur.fetchall()[0]
		journies.append(journey)
		cur = db.cursor()
		cur.execute("SELECT * FROM Reflection WHERE journeyid = (%s)", (x))
		if cur.rowcount:
			reflection = cur.fetchall()[0]
			reflections[journey['event']] = reflection
	return render_template('profile.html', username = username, bio = bio, userjournies = userjournies, journies = journies, reflections=reflections)


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
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(host='0.0.0.0', port=4000, debug=True)
