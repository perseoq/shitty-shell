import cmd, os , curses, sys, stat, datetime

'''
Foreground (text) colors:
\033[30m: Black
\033[31m: Red
\033[32m: Green
\033[33m: Yellow
\033[34m: Blue
\033[35m: Magenta
\033[36m: Cyan
\033[37m: White
Background colors:

\033[40m: Black
\033[41m: Red
\033[42m: Green
\033[43m: Yellow
\033[44m: Blue
\033[45m: Magenta
\033[46m: Cyan
\033[47m: White
'''


class Shitty(cmd.Cmd):
    prompt = 'shitty> '

    
    def do_c(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_l(self, args):
        files = os.listdir('.')
        color = '\033[31m'
        for file in files:
            if file.startswith('.'):
                continue 
            # print("") # esto es un ls nomal, a partir de aqui es el ls -l
            stat_info = os.stat(file)
            size = stat_info.st_size
            permissions = stat.filemode(stat_info.st_mode)
            mtime = datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            print(f'{permissions}  {size:6d}  {mtime} {color}{file}\033[0m')


    def do_x(self, args): # Esto hace que se pueda salir con exit
        sys.exit()
    
    def do_EOF(self, args): # Ctrl + D
        print(" ")
        sys.exit()

    def do_m(self, directory):
        color_e = '\033[31m'
        color_s = '\033[32m'
        reset = '\033[0m'
        try:
            os.mkdir(directory)
            print(f"Directory {color_s}{directory}{reset} created successfully.")
        except OSError as error:
            print(f"Failed to create directory {color_e}{directory}{reset}. Error: {color_e}{error}{reset}")

    def do_d(self, directory):
        color_e = '\033[31m'
        color_s = '\033[32m'
        reset = '\033[0m'
        try:
            os.rmdir(directory)
            print(f"Directory {color_s}{directory}{reset} deleted successfully.")
        except OSError as error:
            print(f"Failed to delete directory {color_e}{directory}{reset}. Error: {color_e}{error}{reset}")

    def do_r(self, args):
        color_e = '\033[31m'
        color_s = '\033[32m'
        reset = '\033[0m'
        files = args.split()
        for file in files:
            try:
                os.remove(file)
                print(f"File {color_s}{file}{reset} deleted successfully.")
            except OSError as error:
                print(f"Failed to delete file {color_e}{file}{reset}. Error: {color_e}{error}{reset}")

    def do_f(self, filename):
        color_e = '\033[31m'
        color_s = '\033[32m'
        reset = '\033[0m'
        try:
            with open(filename, 'a'):
                os.utime(filename, None)
                print(f"File {color_s}{filename}{reset} created successfully.")
        except OSError as error:
            print(f"Failed to create file {color_e}{filename}{reset}. Error: {color_e}{error}{reset}")
    
    def do_e(self, directory):
        color_e = '\033[31m'
        color_s = '\033[32m'
        reset = '\033[0m'
        try:
            os.chdir(directory)
            print(f"Changed directory to {color_s}{directory}{reset}")
        except OSError as error:
            print(f"Failed to change directory to {color_e}{directory}{reset}. Error: {color_e}{error}{reset}")

    def do_help(self, arg):
        color = '\033[36m'
        reset = '\033[0m'
        commands = {
            "l": "   List files and directories",
            "m": f"   Usage: {color}m <directory>{reset} (Create a directory)",
            "e": f"   Usage: {color}e <directory>{reset} (Change the current working directory)",
            "d": f"   Usage: {color}d <directory>{reset} (Delete a directory)",
            "f": f"   Usage: {color}f <filename>{reset} (Create an empty file)",
            "r": f"   Usage: {color}r <filename>{reset} (Delete a file)",
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
    try:
        Shitty().cmdloop()
    except KeyboardInterrupt:
            print('')
