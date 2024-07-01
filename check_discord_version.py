# Import the os module
import os
import json
import subprocess

# Import the color.py file
from utils.color import Colors, BackColors, color_text
from utils.request_utils import make_http_request, get_last_version_from_url
from utils.utils import grep_line_in_file, get_command_line_argument, check_final_version


def get_lastest_discord_version(url: str):
	response = make_http_request(url, "GET", None, {'Content-Type': 'application/json'})
	data = json.loads(response)
	current_version = data['version']
	print(f"Latest Discord version: {current_version}")


def get_local_discord_version(local_path: str):
	# update_exe_path = os.path.join(os.environ['LOCALAPPDATA'], 'Discord', 'Update.exe')
	update_exe_path = os.path.join(local_path, 'Discord', 'Update.exe')
	
	if not os.path.exists(update_exe_path):
		print("Discord n'est pas installé dans le chemin standard.")
		return None
	
	try:
		version = subprocess.check_output([update_exe_path, '--version'], text=True).strip()
		return version
	except subprocess.CalledProcessError as e:
		print(f"Erreur lors de la récupération de la version de Discord: {e}")
		return None

	version = get_local_discord_version()
	if version:
		print(f"La version locale de Discord est : {version}")
	else:
		print("Impossible de récupérer la version de Discord.")

def check_discord_version(url: str):
	lastest_version = get_lastest_discord_version(url)
	# local_version = get_local_discord_version()
	# check_final_version(lastest_version, local_version, "Discord")

