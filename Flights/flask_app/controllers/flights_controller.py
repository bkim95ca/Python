from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User

bcrypt =  Bcrypt(app)


# @app.route('/users/register', methods=['POST'])
# def register():
#     if not User.validate(request.form):
#         return redirect('/')
#     hashed_pass = bcrypt.generate_password_hash(request.form['password'])
#     data = {
#         **request.form,
#         'password' : hashed_pass
#     }
#     id = User.create(data)
#     session['user_id'] = id
#     return redirect('/welcome')

@app.route('/home')
def flights_home():
    return render_template("home.html")
