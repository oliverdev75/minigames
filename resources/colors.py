from colorama import Fore, Back, Style

def reset() -> None:
    """
    Resets all console styles
    """
    print(Style.RESET_ALL, end="")

def colored(color, new_line: bool) -> None:
    """
    Turns colored background and white foreground on
    
    Parameters:
        color: Is the color that is enabled in console background
        new_line (bool): Indicates if the message has to has a line above
    """
    if new_line:
        print()
    print(color + Fore.WHITE, end="")


def blue(new_line: bool = True) -> None:
    """
    Turns blue background and white foreground on

    Parameters:
        new_line (bool): Indicates if the message has to has a line above
    """
    colored(Back.BLUE, new_line)


def red(new_line: bool = True) -> None:
    """
    Turns red background and white foreground on
    
    Parameters:
        new_line (bool): Indicates if the message has to has a line above
    """
    colored(Back.RED, new_line)


def yellow(new_line: bool = True) -> None:
    """
    Turns yellow background and white foreground on
    
    Parameters:
        new_line (bool): Indicates if the message has to has a line above
    """
    colored(Back.YELLOW, new_line)


def green(new_line: bool = True) -> None:
    """
    Turns green background and white foreground on
    
    Parameters:
        new_line (bool): Indicates if the message has to has a line above
    """
    colored(Back.GREEN, new_line)