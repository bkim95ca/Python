from flask import Flask, render_template, session
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'we can change this!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<word>')
#path variabels go in <>
def say_word(word):
    #remember to bring your path variables in as parameters

    return "Hi " + word.capitalize() + "!"


@app.route('/say/<int:num>/<word>')
#path variabels go in <>
def say_words(num, word):
    #remember to bring your path variables in as parameters
    capitalized = word.capitalize()
    return int(num) * str(capitalized)

@app.errorhandler(404)
def handle_bad_request(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)