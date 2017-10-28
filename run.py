#!/usr/bin/env python
import os
import signal
from app.watchsass import WatchSass
from subprocess import Popen

debug = True
flask_run = None


def run_flask(debug=False):
    global flask_run
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.environ["FLASK_APP"] = dir_path + "/app/main.py"
    if debug:
        os.environ["FLASK_DEBUG"] = "1"
    flask_run = Popen(['flask', 'run'])
    flask_run.wait()


def kill_flask(signum, frame):
    global flask_run
    signal.signal(signal.SIGINT, original_sigint)
    print("Shutting Down Flask")
    flask_run.kill


if __name__ == "__main__":
    # Override Ctrl+C to allow graceful shutdown of flask and Sass
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, kill_flask)

    if debug:
        with WatchSass(input_dir="app/static/sass", output_dir="app/static/css"):
            run_flask(debug)
    else:
        run_flask(debug)
