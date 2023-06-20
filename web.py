from flask import Flask, redirect, session, url_for, render_template, request, flash
import requests
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///register_log.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter((User.username == username) | (User.email == username)).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('You are logged in', 'success')
        else:
            if not user:
                flash('Your username/email is incorrect', 'error')
            else:
                flash('Your password is incorrect', 'error')
    
    return render_template('login.html')
    

@app.route('/user')
def user():
    return render_template('user.html')
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'

@app.route('/fun', methods=['POST', 'GET'])
def fun():
    if request.method == 'POST' and 'get_joke' in request.form:
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        result = response.json()
        joke_actually = result["value"]
        return render_template('fun.html', joke=joke_actually)

    return render_template('fun.html')

@app.route('/Registration',methods=['GET', 'POST'])
def reg():
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        user_email = User.query.filter_by(email=email).first()
        user_username = User.query.filter_by(username=username).first()
        if user_email and user_username:
            flash('This user already exists. Please log in.', 'error')
            return redirect(url_for('login'))
        elif user_email:  
            flash('This email  is already in use', 'error')
            return redirect(url_for('reg'))
        elif user_username:
            flash('This username is already in use', 'error')
            return redirect(url_for('reg'))
        
        else:
            session['username'] = username
            user = User()
            user.email = request.form['email']
            user.username = request.form['username']
            user.password = generate_password_hash(request.form['password'])
            db.session.add(user)
            db.session.commit()

            flash('User registered successfully', 'success')
            return redirect(url_for('user'))
    
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug = True)