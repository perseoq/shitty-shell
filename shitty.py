import cmd
import os
import sys

class Shitty(cmd.Cmd):
    prompt = 'shitty> '

    def do_ls(self, args):
        files = os.listdir('.')
        for file in files:
            print(file)

    def do_mkdir(self, directory):
        try:
            os.mkdir(directory)
            print(f"Directory {directory} created successfully.")
        except OSError as error:
            print(f"Failed to create directory {directory}. Error: {error}")

    def do_rmdir(self, directory):
        try:
            os.rmdir(directory)
            print(f"Directory {directory} deleted successfully.")
        except OSError as error:
            print(f"Failed to delete directory {directory}. Error: {error}")

    def do_touch(self, filename):
        try:
            with open(filename, 'a'):
                os.utime(filename, None)
                print(f"File {filename} created successfully.")
        except OSError as error:
            print(f"Failed to create file {filename}. Error: {error}")


if __name__ == '__main__':
    Shitty().cmdloop()
