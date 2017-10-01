#!/usr/bin/env python
from app.main import app
from sys import argv

if "-d" in argv or "--debug" in argv:
    debug = True
else:
    debug = False

app.run(debug=debug)
