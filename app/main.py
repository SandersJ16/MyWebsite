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


def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('app.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


app = CustomTemplateFlask(__name__)
register_blueprints(app)
