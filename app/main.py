from werkzeug.utils import find_modules, import_string
from flask import Flask, render_template
from flask_jsglue import JSGlue
import jinja2


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

    def render_template(self, template_path, **kwargs):
        full_template_path = self.config.template_type + '/' + template_path
        try:
            rendered = render_template(full_template_path, **kwargs)
        except jinja2.exceptions.TemplateNotFound:
            full_template_path = self.config.default_template_type + '/' + template_path
            rendered = render_template(full_template_path, **kwargs)
        return rendered


def register_blueprints(app):
    for name in find_modules('blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def load_global_configuration(app):
    app.config.user = None
    app.config.default_template_type = 'jinja'
    app.config.template_type = 'jinja'


@jinja2.contextfunction
def get_context(context):
    return context


app = CustomTemplateFlask(__name__)
load_global_configuration(app)
app.jinja_env.globals['context'] = get_context
app.jinja_env.globals['callable'] = callable
app.jinja_env.globals['vars'] = vars
register_blueprints(app)
jsglue = JSGlue(app)

# if app.debug:
#     sass(app, input_dir='static/sass/')

# @app.cli.command()
# def initdb():
#     """Initialize the database."""
#     click.echo('Init the db')
