from werkzeug.utils import find_modules, import_string
from flask import Flask


class CustomTemplateFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

    def __init__(self, name):
        super().__init__(name)
        self.jinja_env.add_extension('jinja2.ext.do')


def register_blueprints(app):
    """
    Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def load_global_configuration(app):
    app.config.user = None


app = CustomTemplateFlask(__name__)
load_global_configuration(app)
register_blueprints(app)
# if app.debug:
#     sass(app, input_dir='static/sass/')

# @app.cli.command()
# def initdb():
#     """Initialize the database."""
#     click.echo('Init the db')
