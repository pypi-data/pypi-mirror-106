from ansi.color import fg, fx

PRINT_LEVELS = {"fatal": fg.red, "warning": fg.yellow, "info": fg.green}

def fprint(text, level="info"):
    print(PRINT_LEVELS.get(level.lower(), lambda x: x)(text) + str(fx.reset))

def info(text): fprint(text, "info")

def warning(text): fprint(text, "warning")

def fatal(text): fprint(text, "fatal")