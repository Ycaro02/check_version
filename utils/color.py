#!/usr/bin/env python3
from colorama import init, Fore, Style, Back

# Init colorama
init(autoreset=True)

class Colors:
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    PINK = Fore.LIGHTMAGENTA_EX
    WHITE = Fore.WHITE
    LIGHTBLACK_EX = Fore.LIGHTBLACK_EX
    LIGHTRED_EX = Fore.LIGHTRED_EX
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
    LIGHTBLUE_EX = Fore.LIGHTBLUE_EX
    LIGHTCYAN_EX = Fore.LIGHTCYAN_EX
    LIGHTWHITE_EX = Fore.LIGHTWHITE_EX
    RESET = Style.RESET_ALL

class BackColors:
	BLACK = Back.BLACK
	RED = Back.RED
	GREEN = Back.GREEN
	YELLOW = Back.YELLOW
	BLUE = Back.BLUE
	MAGENTA = Back.MAGENTA
	CYAN = Back.CYAN
	WHITE = Back.WHITE
	PINK = Back.LIGHTMAGENTA_EX
	LIGHTBLACK_EX = Back.LIGHTBLACK_EX
	LIGHTRED_EX = Back.LIGHTRED_EX
	LIGHTGREEN_EX = Back.LIGHTGREEN_EX
	LIGHTYELLOW_EX = Back.LIGHTYELLOW_EX
	LIGHTBLUE_EX = Back.LIGHTBLUE_EX
	LIGHTCYAN_EX = Back.LIGHTCYAN_EX
	LIGHTWHITE_EX = Back.LIGHTWHITE_EX
	RESET = Style.RESET_ALL

def color_text(text : str, color : str):
	return f"{color}{text}{Colors.RESET}"

# Test function
def test_all_color():
	print(f"{Colors.RED}Red text{Colors.RESET}")
	print(f"{Colors.MAGENTA}Magenta text{Colors.RESET}")
	print(f"{Colors.GREEN}Green text{Colors.RESET}")
	print(f"{Colors.YELLOW}Yellow text{Colors.RESET}")
	print(f"{Colors.CYAN}Cyan text{Colors.RESET}")
	print(f"{Colors.BLUE}Blue text{Colors.RESET}")
	print(f"{Colors.PINK}Pink text{Colors.RESET}")
	print(f"{Colors.LIGHTBLACK_EX}Light black text{Colors.RESET}")
	print(f"{Colors.LIGHTRED_EX}Light red text{Colors.RESET}")
	print(f"{Colors.LIGHTGREEN_EX}Light green text{Colors.RESET}")
	print(f"{Colors.LIGHTYELLOW_EX}Light yellow text{Colors.RESET}")
	print(f"{Colors.LIGHTBLUE_EX}Light blue text{Colors.RESET}")
	print(f"{Colors.LIGHTCYAN_EX}Light cyan text{Colors.RESET}")
	print(f"{Colors.LIGHTWHITE_EX}Light white text{Colors.RESET}")
	print(f"{Colors.WHITE}White text{Colors.RESET}")
	print(f"{Colors.RESET}Reset text{Colors.RESET}")


def test_all_back_test():
	print(f"{BackColors.RED}Red text{BackColors.RESET}")
	print(f"{BackColors.MAGENTA}Magenta text{BackColors.RESET}")
	print(f"{BackColors.GREEN}Green text{BackColors.RESET}")
	print(f"{BackColors.YELLOW}Yellow text{BackColors.RESET}")
	print(f"{BackColors.CYAN}Cyan text{BackColors.RESET}")
	print(f"{BackColors.BLUE}Blue text{BackColors.RESET}")
	print(f"{BackColors.PINK}Pink text{BackColors.RESET}")
	print(f"{BackColors.LIGHTBLACK_EX}Light black text{BackColors.RESET}")
	print(f"{BackColors.LIGHTRED_EX}Light red text{BackColors.RESET}")
	print(f"{BackColors.LIGHTGREEN_EX}Light green text{BackColors.RESET}")
	print(f"{BackColors.LIGHTYELLOW_EX}Light yellow text{BackColors.RESET}")
	print(f"{BackColors.LIGHTBLUE_EX}Light blue text{BackColors.RESET}")
	print(f"{BackColors.LIGHTCYAN_EX}Light cyan text{BackColors.RESET}")
	print(f"{BackColors.LIGHTWHITE_EX}Light white text{BackColors.RESET}")
	print(f"{BackColors.WHITE}White text{BackColors.RESET}")
	print(f"{BackColors.RESET}Reset text{BackColors.RESET}")
