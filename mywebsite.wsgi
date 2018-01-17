#!/usr/bin/python
import os
import sys
import logging

sys.path.insert(0, "/var/www/MyWebsite/app/")
from main import app as application

logging.basicConfig(stream=sys.stderr)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "secret_key"), "r") as f:
    secret_key = f.read()
    application.secret_key = secret_key
