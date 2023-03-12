from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def Hello_world():
    return render_template("home_page.html")

@app.route("/jobs_done/")

def works_page():
    return render_template('Experiences.html')

if __name__ == "__main__":
    app.run(debug=True)