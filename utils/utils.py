# Import the sys module
import sys

from utils.color import Colors, BackColors, color_text

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


def get_first_command_line_args():
	"""
	Get the command line argument

	Returns:
	- str: The first command line argument.
	"""
	if len(sys.argv) != 2:
		print(f"{Colors.RED}Usage: python3 test.py <Chemin du dossier League of Legends>\n Souvent : C:/Riot Games/League of Legends ou /home/utilisateur/Riot Games/League of Legends{Colors.RESET}")
		sys.exit(1)
	return sys.argv[1]

def check_version_equal(latest_version: str, local_version: str, app_name: str):
	"""
	Check the final version of League of Legends

	Parameters:
	- latest_version (str): The URL receive version
	- local_version (str): The local version.
	"""
	if local_version == latest_version:
		print(f"{Colors.GREEN}La version de {app_name} est à jour{Colors.RESET}")
	else:
		print(f"{Colors.RED}Une nouvelle version de {app_name} est disponible {Colors.RESET}")

def check_version_greater_equal(latest_version: str, local_version: str, app_name: str):
	"""
	Check the final version of League of Legends

	Parameters:
	- latest_version (str): The URL receive version
	- local_version (str): The local version.
	"""
	if local_version > latest_version:
		print(f"{Colors.GREEN}La version de {app_name} installée est plus récente que la dernière version disponible.{Colors.RESET}")
		return ;
	check_version_equal(latest_version, local_version, app_name)


