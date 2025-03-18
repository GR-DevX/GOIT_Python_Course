from colorama import Fore, Style, init

init(autoreset=True)

def log_message(lvl,message):
    lvl=lvl.upper()
    COLORS={
        'DEBUG'     :Fore.BLUE,
        'INFO'      :Fore.GREEN,
        'WARNING'   :Fore.YELLOW,
        'ERROR'     :Fore.RED,
        'CRITICAL'  :Fore.MAGENTA,
    }
    if lvl in COLORS.keys():
        return f"{COLORS[lvl]} {lvl}: {Style.RESET_ALL}{message}"
    else:
        return f"{Fore.WHITE}{lvl}: {message}{Style.RESET_ALL}"

def debug(message):
    return log_message('DEBUG',message)

def info(message):
    return log_message('info',message)

def warn(message):
    return log_message('warning',message)

def error(message):
    return log_message('error',message)

def crit(message):
    return log_message('critical',message)


if __name__=="__main__":
    print(debug('DEBUG'))
    print(info('INFO'))
    print(warn('WARNING'))
    print(error('ERROR'))
    print(crit('CRITICAL'))