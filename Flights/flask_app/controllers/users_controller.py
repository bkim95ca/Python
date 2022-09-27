import re
from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

@app.route('/')
def flights_splash():
    # logged_user = User.get_by_id({'id' : session['user_id']})
    return render_template("index.html")

@app.route('/register')
def registration_page():
    return render_template("register.html")

@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/register')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/home')

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/users/login', methods=['POST'])
def login():
    #see if the username/email provided exists in the database
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user is not registered
    if not user_in_db:
        flash("Invalid login info", "log")
        return redirect('/login')
    #if the user exists, check the password
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid login info", "log")
        return redirect('/login')
    #log them in
    session['user_id'] = user_in_db.id
    return redirect('/home')

@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')