from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def new_ninja_form():
    all_dojos = Dojo.get_all()
    return render_template("ninja.html", all_dojos = all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    request.form["dojo_id"]
    return redirect('/dojos')

