from flask import Blueprint, render_template

bp = Blueprint("views", __name__, template_folder="templates")


@bp.route("/")
@bp.route("/index")
def index():
    user = {"nickname": "Sandy"}
    return render_template("index.htm.j2",
                           title="Grand Code Master Supreme",
                           user=user)
