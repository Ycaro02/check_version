# Import the os module
import os
import json
import requests

# Import the color.py file
from utils.color import Colors, BackColors, color_text
from utils.request_utils import make_http_request, get_last_version_from_url
from utils.utils import grep_line_in_file, get_command_line_argument, check_final_version

# Import the re module for regular expressions
import re
# pip install beautifulsoup4 for parse elements from html
from bs4 import BeautifulSoup


def get_local_discord_version():
	discord_base_path = os.path.join(os.environ['LOCALAPPDATA'], 'Discord')
	if not os.path.exists(discord_base_path):
		print("Discord n'est pas installé dans le chemin standard.")
		return None

	# List all directories in the Discord directory
	discord_versions = [d for d in os.listdir(discord_base_path) if os.path.isdir(os.path.join(discord_base_path, d)) and d.startswith('app-')]

	# Use a regular expression to extract the version numbers and sort them
	version_pattern = re.compile(r'app-(\d+\.\d+\.\d+)')
	versions_sorted = sorted(discord_versions, key=lambda x: [int(num) for num in version_pattern.match(x).groups()[0].split('.')], reverse=True)

	if versions_sorted:
		latest_version = versions_sorted[0].split('-')[1]
		print(f"La version la plus récente de Discord installée est : {latest_version}")
		return latest_version
	else:
		print("Aucune version de Discord trouvée.")
		return None


def get_lastest_discord_version(url: str):
	response = requests.get(url)
	
	# Use BeautifulSoup to parse the HTML content
	soup = BeautifulSoup(response.text, 'html.parser')
	
	# Search for the element containing the version with the class 'version'
	version_element = soup.find('div', class_='version')
	
	if version_element:
		# Extract the text from the element and clean the string if necessary
		version_text = version_element.text.strip()
		
		# Use a regular expression to extract the numeric version
		version_match = re.search(r'\d+\.\d+\.\d+', version_text)
		if version_match:
			latest_version = version_match.group(0)
			print(f"La dernière version de Discord est : {latest_version}")
			return latest_version
		else:
			print("Impossible d'extraire la version de Discord.")
	else:
		print("Élément contenant la version non trouvé.")


def check_discord_version(url: str):
	lastest_version = get_lastest_discord_version(url)
	local_version = get_local_discord_version()
	check_final_version(lastest_version, local_version, "Discord")

