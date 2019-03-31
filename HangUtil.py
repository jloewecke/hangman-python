import os
import enum
from colorama import init, Fore, Back, Style

# Must init colorama, on pre windows 10 machines
init(autoreset=True)

class MsgError(enum.Enum):
	Info = 1
	Warn = 2
	Error = 3
	Fatal = 4

def clear_screen():
	if os.name == 'nt':
		os.system("cls")
	else:
		os.system("clear")

def print_row(puzzle, guessed, turns):
	print("{:25} {:26} {:>15}".format(puzzle, guessed, turns))

def print_msg(level, msg):
	if level == MsgError.Info.name:
		msg_color = Style.BRIGHT
	elif level == MsgError.Warn.name:
		msg_color = Back.YELLOW + Style.BRIGHT
	elif level == MsgError.Error.name:
		msg_color = Back.RED + Fore.WHITE
	elif level == MsgError.Fatal.name:
		msg_color = Back.WHITE + Fore.RED + Style.BRIGHT
	else:
		fatal_err = print(Back.RED + Fore.RED +
			" Programer BrainDamage: " +
			level + " is an invalid option ")
		input("Hit 'Enter' to continue")

	print(msg_color + msg)
