from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

# Display the form
@app.route("/")
def hello():
    return render_template("index.html")

# Handle form submission
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return render_template("thanks.html")

app.run(debug=True)
