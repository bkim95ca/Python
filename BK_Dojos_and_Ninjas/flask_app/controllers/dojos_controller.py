from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo_model import Dojo

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    return render_template('dojo.html', all_dojos = all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():   
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def one_dojo(id):
    one_dojo = Dojo.get_ninja_with_awards({'id' : id})
    return render_template('one_dojo.html', one_dojo = one_dojo)