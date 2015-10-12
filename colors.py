def color(string, color='', graphic=''):
    """
    Change text color for the Linux terminal.

    Args:
        string (str): String to colorify
        color (str): Color to colorify the string in the following list:
            black, red, green, yellow, blue, purple, cyan, gr[ae]y
        graphic (str): Graphic to append to the beginning of the line
    """

    colors = {
    'normal'         : "\x1b[0m",
    'black'          : "\x1b[30m",
    'red'            : "\x1b[31m",
    'green'          : "\x1b[32m",
    'yellow'         : "\x1b[33m",
    'blue'           : "\x1b[34m",
    'purple'         : "\x1b[35m",
    'cyan'           : "\x1b[36m",
    'grey'           : "\x1b[90m",
    'gray'           : "\x1b[90m",
    'bold'           : "\x1b[1m"
    }

    if not color:
        if string.startswith("[!] "): 
            color = 'red'
        elif string.startswith("[+] "): 
            color = 'green'
        elif string.startswith("[*] "): 
            color = 'blue'
        else:
            color = 'normal'

    if color not in colors:
        print colors['red'] + 'Color not found: {}'.format(color) + colors['normal']
        return

    if color:
        return colors[color] + graphic + string + colors['normal']
    else:
        return string + colors['normal']

