from os import system, name, path
import string

from colorama import Fore


def log(output):
    my_path = "debug.txt"
    if path.exists(my_path):
        append_write = 'a'
    else:
        append_write = 'w'

    f = open(my_path, append_write)
    f.write(output + "\n")
    f.close()

def chunks(s, n):
    lines = []
    s = s.split()
    temp = ''
    for line in s:
        if len(temp) < n:
            temp += line + " "
        else:
            lines.append(temp)
            temp = ""
            temp += line + ' '
    lines.append(temp)
    return lines


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


def center_align(data):
    final_string = ""
    lines = chunks(data, 40)
    for line in lines:
        textSize = len([c for c in line if c in string.printable])
        dif = 50 - textSize
        padding = ' ' * int(dif / 2)
        final_string += padding + line + '\n'
    return final_string

def get_color_str(char, color):
    colors = {
        "blue": Fore.BLUE,
        "green": Fore.GREEN,
        "magenta": Fore.MAGENTA,
        "red": Fore.RED,
        "yellow": Fore.YELLOW,
    }
    return colors.get(color, "") + char + Fore.RESET

def getch():
    """
    Interrupting program until pressed any key
    """
    try:
        import msvcrt
        x = bytes.decode(msvcrt.getch())
        return x

    except ImportError:
        print("This program must be run on Windows")
