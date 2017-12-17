from flask import Blueprint, render_template, current_app as app

bp = Blueprint("views", __name__, template_folder="templates")


@bp.route("/")
@bp.route("/index")
@bp.route("/home")
def index():
    return render_template("home.htm.j2",
                           title="Justin Sanders",
                           subtitle="Grand Code Master Supreme")

@bp.route("/about")
def about():
    return render_template("about.htm.j2")

@bp.route("/resume")
def resume():
    return render_template("resume.htm.j2")
