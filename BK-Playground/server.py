from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html", phrase="Welcome!")

# def play():
#     boxes=3
#     return render_template("index.html", color="white", boxes=boxes)

# def number(num):
#     boxes = num
#     return render_template("index.html", boxes=boxes)

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def assign_color(num=3, color="white"):
    boxes = num
    return render_template("index.html", boxes=boxes, color = color)

if __name__ == "__main__":
    app.run(debug=True)