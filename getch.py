def getch():
    """
    Interrupting program until pressed any key
    """
    try:
        import msvcrt
        x = bytes.decode(msvcrt.getch())
        return x

    except ImportError:
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
