from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html") 

@app.route('/counter', methods=['POST'])
def counter():
    # session['click'] = request.form['click']
    # session['reset'] = request.form['reset']
    if request.form['click'] == 'add_two':
        session['count'] += 1
        
    return redirect('/')

@app.route('/clear_session')
def clear_session():
    session.clear() #would remove all keys
    # del session['dog_breed'] would remove one key
    # dog_name = session.pop('dog_name')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)