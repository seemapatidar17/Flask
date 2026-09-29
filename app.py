from email.policy import default

from flask import Flask, render_template, request
#from uuid import UUID

app = Flask(__name__)
"""
@app.route("/")
def home():
    return "Home page"

@app.route("/user/<string:name>")
def user(name):
    return f" User ID : {name}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

#QUERY PARAMETERS
@app.route("/search")
def search():
    name = request.args.get("name","Guest")
    course = request.args.get("course","Python")
    return f"Hello {name}, you are enrolled in {course}"
"""

@app.route("/")
def home():
    name = "Anish"
    course = "Flask"
    city = "Bhopal"
    age = "20"
    return render_template("index.html", name=name, course=course, city=city, age=age) 

if __name__ == "__main__":
    app.run(debug=True)

