# debug functions for old school


def log(output):
    f = open("debug.txt", "a")
    f.write(output + "\n")
    f.close()
