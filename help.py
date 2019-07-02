from os import system, name
import string

from colorama import Fore


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