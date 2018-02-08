from flask import Blueprint
import json

bp = Blueprint("filters", __name__, template_folder="templates")


@bp.app_template_filter('to_json')
def to_json(value):
    return json.dumps(value, default=json_handler)


def json_handler(obj):
    try:
        return json.JSONEncoder().default(obj)
    except TypeError:
        return str(obj)
