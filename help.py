from os import system, name


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
    lines = chunks(data, 30)
    for line in lines:
        dif = 50 - len(line)
        padding = ' ' * int(dif / 2)
        final_string += padding + line + '\n'
    return final_string
