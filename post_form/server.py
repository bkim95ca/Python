from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
#import request to be able to access the body of our post requests (request.form)
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "No secrets on github"





@app.route('/')          # The "@" decorator associates this route with the function immediately following
def render_form():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

@app.route('/process_form', methods=['POST']) #methods list for specifying methods to listen for
def process_form():
    print(request.form)
    session['dog_name'] = request.form['dog_name']
    session['dog_breed'] = request.form['dog_breed']
    # if not session['form_num'] == "1" and not session['form_num'] == '2':
    #     print("Hey stop hackin")
    #     return redirect('/')
    session['form_num'] = request.form['form_num']
    # return render_template("display.html", name = name,breed = breed) #typically we won't render on "ACTION ROUTES"
    return redirect("/show_info")

@app.route('/show_info')
def show_info():
    if 'form_num' in session:
        num = session['form_num']
    # name = session['dog_name']
    # breed = session['dog_breed']
    return render_template("display.html", num=num)

@app.route('/clear_session')
def clear_session():
    session.clear() #would remove all keys
    # del session['dog_breed'] would remove one key
    # dog_name = session.pop('dog_name')
    return redirect('/')








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.