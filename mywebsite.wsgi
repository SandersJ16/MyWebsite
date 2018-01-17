#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/MyWebsite/app/")

print(sys.version_info)

from main import app as application
with open("secret_key", "r") as f:
    secret_key = f.read()
    application.secret_key = secret_key
