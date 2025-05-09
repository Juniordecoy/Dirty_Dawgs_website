from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

@app.route("/", methods=["GET","POST"])
def home():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)