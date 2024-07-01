# Import the os module
import os

# Import the color.py file
from utils.color import Colors, BackColors, color_text
from utils.request_utils import make_http_request, get_last_version_from_url
from utils.utils import grep_line_in_file, get_command_line_argument, check_final_version

def get_last_lol_locale_version(path: str):
	"""
	Retrieves the last local version of League of Legends from the game configuration file.

	Parameters:
	- path (str): The base path where the game configuration file is located.

	Returns:
	- str: The last local version of the game, or None if an error occurs.
	"""
	try:
		# Construct the path to the configuration file
		file_path = os.path.join(path, "Config", "game.cfg")
		
		# Use the grep_line_in_file function to find the line containing "Version"
		file_content = grep_line_in_file(file_path, "Version")
		
		# Check if file_content is not None
		if file_content:
			try:
				# Attempt to extract the local version
				parts = file_content.split("=")[1].split('.')
				local_version = parts[0] + "." + parts[1]
			except IndexError:
				# Handle the case where the line format is not as expected
				print(f"Error: The version format in the file {file_path} is incorrect.")
				return None
		else:
			# Handle the case where the "Version" line is not found
			print(f"Error: The line containing 'Version' was not found in {file_path}.")
			return None
		
		# Print the found local version
		print(f"{Colors.YELLOW}Dernière version {local_version}, d'après le fichier {file_path}{Colors.RESET}")
		return local_version
	except Exception as e:
		# Handle unexpected exceptions
		raise e
		return None

def check_league_of_legend_version(url: str):
	"""
	Check the version of League of Legends

	Parameters:
	- url (str): The URL to check the version of League of Legends.
	"""
	last_version = get_last_version_from_url(url)
	truncate_version = last_version.split('.')[0] + "." + last_version.split('.')[1]
	local_version = get_last_lol_locale_version(get_command_line_argument())

	check_final_version(truncate_version, local_version, "League of Legends")
