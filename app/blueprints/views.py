from flask import Blueprint, current_app as app

bp = Blueprint("views", __name__, template_folder="templates")


@bp.route("/")
@bp.route("/index")
@bp.route("/home")
def index():
    return app.render_template("home.htm.j2",
                               title="Justin Sanders",
                               subtitle="Grand Code Master Supreme")

@bp.route("/about")
def about():
    return app.render_template("about.htm.j2")


@bp.route("/resume")
def resume():
    return app.render_template("new_resume.htm.j2")
