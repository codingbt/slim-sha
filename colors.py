class Color():
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[54m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[91m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def color_reset():
    print(Color.END)
