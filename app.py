from flask import Flask, session,url_for,redirect,render_template,request


app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def index():
    if session.get('user_key',None) is not None:
        return redirect(url_for('/game',user_key=session['user_key']))
    return redirect(url_for('login'))

@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/join',methods=['POST'])
def join():
    room_code = request.form['room-code']
    username = request.form['username']
    return f'Username: {username} <br> Room Code:{room_code}'