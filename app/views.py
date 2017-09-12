from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "Sandy"}
    return render_template("index.htm.j2",
                           title="Grand Code Master Supreme",
                           user=user)
