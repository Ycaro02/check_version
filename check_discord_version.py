# Import the os module
import os
import json
import requests

# Import the color.py file
from utils.color import Colors, BackColors, color_text
from utils.request_utils import make_http_request, get_last_version_from_url
from utils.utils import grep_line_in_file, get_first_command_line_args, check_version_greater_equal

# Import the re module for regular expressions
import re
# pip install beautifulsoup4 for parse elements from html
from bs4 import BeautifulSoup


def get_local_discord_version(path: str = None):
	if str is None:
		discord_base_path = os.path.join(os.environ['LOCALAPPDATA'], 'Discord')
	else:
		discord_base_path = path
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
		# print(f"La version la plus récente de Discord installée est : {latest_version}")
		return latest_version
	else:
		print("Aucune version de Discord trouvée.")
		return None

def get_discord_version():
	url = "https://discord.com/api/download?platform=win"
	response = requests.head(url, allow_redirects=True)
	if response.status_code == 200:
		final_url = response.url
		version = final_url.split('/')[-2]  # Extract version from URL
		return version
	return None

def get_latest_discord_version(channel="stable"):
	url = f"https://discord.com/api/download/{channel}?platform=win"
	response = requests.head(url, allow_redirects=True)
	if response.status_code == 200:
		final_url = response.url
		version = final_url.split('/')[-2]  # Extract version from URL
		return version
	return None


def check_discord_version(url: str):
	latest_version = get_discord_version()
	latest_stable_version = get_latest_discord_version("stable")

	# detect os and fill os_version
	if os.name == "nt": # Windows
		local_version = get_local_discord_version()
	else:				# Linux (test hardpath)
		local_version = get_local_discord_version('/mnt/windows/Users/Ycaro-Win/AppData/Local/Discord')

	if latest_version > latest_stable_version:
		save_latest = latest_version
	else:
		save_latest = latest_stable_version

	if save_latest is None:
		print(color_text("Impossible de récupérer la dernière version de Discord.", Colors.RED))
		return
	
	print(color_text("La version de Discord installée est : " + local_version, Colors.YELLOW))
	print(color_text("La dernière version de Discord disponible est : " + save_latest, Colors.YELLOW))

	if (save_latest is not None) and (local_version is not None):
		check_version_greater_equal(save_latest, local_version, "Discord")