from subprocess import Popen
import os.path


class WatchSass(object):
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def __enter__(self):
        self.sass_process = self.watch_files(self.input_dir, self.output_dir)
        return self.sass_process

    def __exit__(self, exc_type, exc_value, traceback):
        self.sass_process.kill()

    @staticmethod
    def watch_files(input_dir, output_dir):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        sass_executable = dir_path + '/static/node_modules/.bin/node-sass'
        if not os.path.isfile(sass_executable):
            raise Exception("Couldn't find node-sass executable. Be sure you have run `yarn` on your system in developer mode.")
        if not os.path.isdir(input_dir) or not os.path.isdir(output_dir):
            raise Exception("The input and/or output directories supplied are not valid directories.")

        return Popen([sass_executable, '-rw', input_dir, '-o', output_dir])
