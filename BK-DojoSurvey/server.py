from flask import Flask, render_template, request, redirect, session  

app = Flask(__name__)   
app.secret_key = "secretkey"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def render_form():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    session['user_name'] = request.form['user_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")

@app.route('/result')
def show_info():
    return render_template("display.html")

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":     
    app.run(debug=True)    