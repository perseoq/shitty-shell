import cmd
import os
import sys

class Shitty(cmd.Cmd):
    prompt = 'shitty> '

    def do_get(self, args):
        files = os.listdir('.')
        for file in files:
            if file.startswith('.'):
                continue
            print(file)

    def do_make(self, directory):
        try:
            os.mkdir(directory)
            print(f"Directory {directory} created successfully.")
        except OSError as error:
            print(f"Failed to create directory {directory}. Error: {error}")

    def do_del(self, directory):
        try:
            os.rmdir(directory)
            print(f"Directory {directory} deleted successfully.")
        except OSError as error:
            print(f"Failed to delete directory {directory}. Error: {error}")

    def do_file(self, filename):
        try:
            with open(filename, 'a'):
                os.utime(filename, None)
                print(f"File {filename} created successfully.")
        except OSError as error:
            print(f"Failed to create file {filename}. Error: {error}")
    def do_enter(self, directory):
        try:
            os.chdir(directory)
            print(f"Changed directory to {directory}")
        except OSError as error:
            print(f"Failed to change directory to {directory}. Error: {error}")



if __name__ == '__main__':
    Shitty().cmdloop()
