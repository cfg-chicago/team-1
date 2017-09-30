from flask import Flask, render_template, request, redirect, url_for, session
import extensions
import config

app = Flask(__name__, template_folder='templates')
db = extensions.connect_to_database()

@app.route('/')
def index():
    return render_template('home.html')

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
                session['username'] = username
                return redirect(url_for('profile_route', username=session['username']))
            else:
                errors.append("Wrong password")
        return render_template('login.html', errors= errors)
    return render_template('login.html', errors= errors)

@app.route('/logout', methods=['GET', 'POST'])
def logout_route():
    session.pop('username')
    return redirect(url_for('login_route'))

@app.route('/profile', methods=['GET', 'POST'])
def profile_route():
    while True: #Not actually a loop, but we wanna be able to break
        if request.method == 'POST':
            if 'reflection' not in request.form:
                break
            ref = request.form['reflection']
            public = 0
            if 'public' in request.form:
                public = 1
            id = request.form['id']
            cur = db.cursor()
            cur.execute("UPDATE Reflection SET text = (%s), public = (%s) WHERE journeyid = (%s) AND username = (%s)", (ref, public, id, session['username']))
        break
    if 'username' not in session:
            return redirect('403.html', 403)
    username = request.args.get('username')
    if username == None:
        username = session['username']
    cur = db.cursor()
    cur.execute("SELECT * from User WHERE username = (%s)", (username))
    data = cur.fetchall()[0]
    bio = data['bio']
    classid = data['classid']
    pic = data['picture']
    cur = db.cursor()
    cur.execute('''SELECT journeyid FROM UserJourney WHERE username = \"{}\"'''.format(username))
    userjournies = cur.fetchall()
    # Turn tuple of single-tuple items into list
    userjournies = [x['journeyid'] for x in userjournies] 
    journies = []
    reflections = {}
    for x in userjournies:
        cur = db.cursor()
        cur.execute("SELECT * FROM Journey WHERE journeyid = (%s)", (x))
        if cur.rowcount:
            journey = cur.fetchall()[0]
            journies.append(journey)
        cur = db.cursor()
        cur.execute("SELECT * FROM Reflection WHERE journeyid = (%s) AND username = (%s)", (x, username))
        if cur.rowcount:
            reflection = cur.fetchall()[0]
            reflections[journey['event']] = reflection
    return render_template('profile.html', username = username, bio = bio, userjournies = userjournies, journies = journies, reflections=reflections, pic=pic)


@app.route('/journey', methods=['GET', 'POST'])
def journey_route():
    journeyid = request.args.get('journeyid')
    cur = db.cursor()
    cur.execute('''SELECT * FROM Journey''')
    journies = cur.fetchall()
    if journeyid == None:
        return render_template('journey.html', journey_selected=None, journies=journies)

    cur = db.cursor()
    cur.execute("SELECT username, reactiondata FROM Reactions WHERE journeyid = (%s)", (journeyid))
    reacts = cur.fetchall()
    return render_template('journey.html', journey_selected=None, journies=journies, reactions = reacts)

    

@app.route('/class')
def class_route():
    classid = request.args.get('classid')
    cur = db.cursor()
    cur.execute("SELECT * FROM Class")
    classes = cur.fetchall()
    if not classid:
        return render_template('class.html', classes=classes)
    else:
        cur = db.cursor()
        cur.execute("SELECT username FROM User WHERE classid = (%s)", (classid))
        users = cur.fetchall()
        cur = db.cursor()
        cur.execute("SELECT * FROM ClassJourney WHERE classid = (%s)",(classid))
        classjournies = cur.fetchall()
        classjourniesdetails = {}
        for journey in classjournies:
            cur = db.cursor()
            cur.execute("SELECT event FROM Journey WHERE journeyid = (%s)", (journey['journeyid']))
            classjourniesdetails[journey['journeyid']] = cur.fetchall()[0]
        return render_template('class.html', classes = classes, users = users, classjournies = classjournies, classjourniesdetails = classjourniesdetails)

@app.route('/draw')
def draw_route():
    if 'username' not in session:
            return redirect('403.html', 403)

    username = session['username']
    journey = request.args.get('journeyud')
    return render_template('draw.html', journeyid=journey, username=username)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0', port=4000, debug=True)
