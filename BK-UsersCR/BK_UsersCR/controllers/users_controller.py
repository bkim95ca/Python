from BK_UsersCR import app
from flask import Flask, render_template, request, redirect, session
from BK_UsersCR.models.user_model import User

@app.route('/')
def index():
    return render_template('users.html')

@app.route('/user')
def user():
    all_users = User.get_all()
    return render_template('users.html', all_users = all_users)

@app.route('/user/new')
def new_user_form():
    return render_template('new_user.html')

#CREATE NEW USER
@app.route('/user/create', methods=['POST'])
def create_user():
    id = User.add_user(request.form)
    return redirect(f'/user/{id}')

#GET THE USER SELECTED
@app.route('/user/<int:id>')
def one_user(id):
    one_user = User.get_user({'id':id})
    return render_template('one_user.html', one_user = one_user)

#EDIT THE USER 
@app.route('/user/<int:id>/edit')
def edit_user_form(id):
    data = {
        'id': id
    }
    this_user = User.get_user(data)
    return render_template('edit_user.html', this_user = this_user)

@app.route('/user/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form, #quick way to copy the contents of request.form into this dictionary
        'id':id
    }
    User.update(data)
    return redirect('/user')

@app.route('/user/<int:id>/delete')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/user')