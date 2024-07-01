# Import the sys module
import sys

from color import Colors, BackColors, color_text

def grep_line_in_file(file: str, word: str):
	"""
	Grep a line containing a word in a file

	Parameters:
	- file (str): The file to search in.
	- word (str): The word to search for.

	Returns:
	- str: The line containing the word, or None if the word is not found.

	Raises:
	- FileNotFoundError: If the specified file does not exist.
	- PermissionError: If there are not enough permissions to read the file.
	"""
	try:
		with open(file, 'r') as f:
			for line in f:
				if word in line:
					return line
	except FileNotFoundError:
		raise FileNotFoundError(f"The file {file} does not exist.")
	except PermissionError:
		raise PermissionError(f"Permission denied for reading the file {file}.")
	return None


def get_command_line_argument():
	"""
	Get the command line argument

	Returns:
	- str: The first command line argument.
	"""
	if len(sys.argv) != 2:
		print(f"{Colors.RED}Usage: python3 test.py <Chemin du dossier League of Legends>\n Souvent : C:/Riot Games/League of Legends ou /home/utilisateur/Riot Games/League of Legends{Colors.RESET}")
		sys.exit(1)
	return sys.argv[1]

def check_final_version(url_version: str, local_version: str):
	"""
	Check the final version of League of Legends

	Parameters:
	- url_version (str): The URL receive version
	- local_version (str): The local version.
	"""
	if url_version == local_version:
		print(f"{Colors.GREEN}La version est à jour{Colors.RESET}")
	else:
		print(f"{Colors.RED}La version n'est pas à jour{Colors.RESET}")
