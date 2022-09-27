from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dog_model import Dog
from flask_app.models.award_model import Award

@app.route('/awards/new')
def new_award_form():
    all_dogs = Dog.get_all()
    return render_template("award_new.html", all_dogs=all_dogs)

@app.route('/awards/create', methods=['POST'])
def create_award():
    Award.create(request.form)
    id = request.form["dog_id"]
    return redirect(f'/dogs/{id}')

@app.route('/awards')
def all_awards():
    awards = Award.get_all()
    return render_template("awards_all.html", all_awards = awards)

@app.route('/awards/<int:id>')
def one_award(id):
    one_award = Award.get_one({'id' : id})
    return render_template("awards_one.html", one_award = one_award)
