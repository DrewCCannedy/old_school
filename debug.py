# debug functions for old school
import os

def log(output):
    path = "debug.txt"
    if os.path.exists(path):
        append_write = 'a'
    else:
        append_write = 'w'

    f = open(path, append_write)
    f.write(output + "\n")
    f.close()
