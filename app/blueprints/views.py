from flask import Blueprint, render_template, current_app as app

bp = Blueprint("views", __name__, template_folder="templates")


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("home.htm.j2",
                           title="Justin Sanders",
                           subtitle="Grand Code Master Supreme")
