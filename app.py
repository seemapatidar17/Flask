from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/user")
def users():
    return "Welcome to user Page"

@app.route("/user/<name>")
def user(name):
    return f" Hello {name}"

@app.route("/students/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)

