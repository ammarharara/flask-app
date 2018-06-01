from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello2():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
