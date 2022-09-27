
from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.car_model import Car

@app.route('/new')
def new_car_form():
    if 'user_id' not in session:
        return redirect('/')
    # logged_user = User.get_by_id({'id' : session['user_id']})
    return render_template("new_car.html")

@app.route('/new/create', methods=['POST'])
def process_car():
    if 'user_id' not in session:
        return redirect('/')
    if not Car.validator(request.form):
        return redirect('/new')
    data = {
        **request.form,
        'user_id' : session['user_id']
    }
    
    id = Car.create(data)
    return redirect("/dashboard")

@app.route('/edit/<int:id>')
def edit_car(id):
    if 'user_id' not in session: #check to see if the user is in session (or if the user is logged in)
        return redirect('/')
    car = Car.get_by_id({'id': id})
    if not int(session['user_id']) == car.user_id: #if the user id that is logged in is not equal to the party id 
        flash("Cannot edit, please log in.")
        return redirect('/dashboard')
    car = Car.get_by_id({'id':id})
    return render_template("cars_edit.html", car=car)

@app.route('/edit/<int:id>/delete')
def del_car(id):
    if 'user_id' not in session: #check to see if the user is in session (or if the user is logged in)
        return redirect('/')
    Car.get_by_id({'id': id}) #call the party by id
    Car.delete({'id' : id})
    return redirect('/dashboard')

@app.route("/edit/<int:id>/update", methods = ['POST'])
def update_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id': id})
    if not int(session['user_id']) == car.user_id: #if the user id that is logged in is not equal to the id 
        flash("Cannot delete, please log in.")
        return redirect('/dashboard')
    if not Car.validator(request.form):
        return redirect(f"/edit/{id}")
    data = {
        **request.form,
        'id' : id
    }
    Car.update(data)
    return redirect('/dashboard')

@app.route("/show/<int:id>")
def show_party(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id': id})
    return render_template("one_car.html", car = car)


# @app.route('/my_parties')
# def my_parties():
#     if 'user_id' not in session:
#         return redirect('/')
#     logged_user = User.get_by_id({'id': session['user_id']})
#     return render_template("my_parties.html", logged_user=logged_user)

