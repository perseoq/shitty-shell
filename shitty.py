import cmd, os , curses, sys

class Shitty(cmd.Cmd):
    prompt = 'shitty> '

    def do_c(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_l(self, args):
        files = os.listdir('.')
        for file in files:
            if file.startswith('.'):
                continue
            print(file)
    
    def do_x(self, args): # Esto hace que se pueda salir con exit
        sys.exit()
    
    def do_EOF(self, args): # Ctrl + D
        print(" ")
        sys.exit()

    def do_m(self, directory):
        try:
            os.mkdir(directory)
            print(f"Directory {directory} created successfully.")
        except OSError as error:
            print(f"Failed to create directory {directory}. Error: {error}")

    def do_d(self, directory):
        try:
            os.rmdir(directory)
            print(f"Directory {directory} deleted successfully.")
        except OSError as error:
            print(f"Failed to delete directory {directory}. Error: {error}")

    def do_r(self, args):
        files = args.split()
        for file in files:
            try:
                os.remove(file)
                print(f"File {file} deleted successfully.")
            except OSError as error:
                print(f"Failed to delete file {file}. Error: {error}")

    def do_f(self, filename):
        try:
            with open(filename, 'a'):
                os.utime(filename, None)
                print(f"File {filename} created successfully.")
        except OSError as error:
            print(f"Failed to create file {filename}. Error: {error}")
    def do_e(self, directory):
        try:
            os.chdir(directory)
            print(f"Changed directory to {directory}")
        except OSError as error:
            print(f"Failed to change directory to {directory}. Error: {error}")

    def do_help(self, arg):
        commands = {
            "l": "   List files and directories",
            "m": "   Usage: m <directory> (Create a directory)",
            "e": "   Usage: e <directory> (Change the current working directory)",
            "d": "   Usage: d <directory> (Delete a directory)",
            "f": "   Usage: f <filename> (Create an empty file)",
            "r": "   Usage: r <filename> (Delete a file)",
            "c": "   Clear the terminal screen",
            "x": "   Exit the shell",            
        }

        if not arg:
            # Print usage for all commands
            for command, usage in commands.items():
                print(f"{command}: {usage}")
        else:
            # Print usage for a specific command
            if arg in commands:
                print(f"{arg}: {commands[arg]}")
            else:
                print(f"Unknown command: {arg}")

if __name__ == '__main__':
    Shitty().cmdloop()
