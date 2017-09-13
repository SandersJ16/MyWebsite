#!/bin/bash

#Get directory this script lives in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#When true, Sass and scss files will recomplie
#automatically and flask will run in debug mode
development=true

sass_dir="$DIR/app/static/sass"
css_dir="$DIR/app/static/css"
if $development; then
    sass --watch "$sass_dir:$css_dir" &
    python "$DIR/start_flask.py" --debug
else
    sass --update "$sass_dir:$css_dir"
    python "$DIR/start_flask.py"
fi

#Make sure we kill all child jobs spun up by this (Like sass --watch)
trap 'kill $(jobs -p)' EXIT
