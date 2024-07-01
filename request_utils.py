# Import the requests module
import requests

from color import Colors, BackColors, color_text


def make_http_request(url: str, method: str, data: str = None, headers: str =None):
	"""
	Sends an HTTP request to the specified URL and returns the response content as a string.

	Parameters:
	- url (str): The URL to which the request is sent.
	- method (str): The HTTP method to use for the request. Defaults to "GET".
	- data (Optional[dict]): The data to send in the body of the request. Only used for POST requests. Defaults to None.
	- headers (Optional[dict]): Additional headers to send with the request. Defaults to None.

	Returns:
	- str: The response content from the server.

	Raises:
	- ValueError: If the specified HTTP method is not supported.
	- requests.exceptions.RequestException: For network-related errors.
	"""
	try:
		# Choose the HTTP method
		if method == "GET":
			response = requests.get(url, headers=headers)
		elif method == "POST":
			response = requests.post(url, data=data, headers=headers)
		elif method == "PUT":
			response = requests.put(url, data=data, headers=headers)
		elif method == "DELETE":
			response = requests.delete(url, headers=headers)
		else:
			return "Unsupported HTTP method"
		
		if response.status_code != 200:
			print(f"{Colors.RED}HTTP error: {response.status_code}{Colors.RESET}")
			raise requests.exceptions.RequestException(f"HTTP error: {response.status_code}")
		# Return the response text or status code
		return response.text
	except Exception as e:
		raise e

def get_last_version_from_url(url: str):
	"""
	Get the last version from the URL

	Parameters:
	- url (str): The URL to get the last version from.

	Returns:
	- str: The last version from the URL, or an error message if an exception occurs.
	"""
	headers = {'Content-Type': 'application/json'}  # Optional headers
	try:
		response = make_http_request(url, "GET", None, headers)
		# response = requests.get(url).text
		try:
			last_version = response.split('"')[1]
			print(f"{Colors.YELLOW}Dernière version {last_version}, d'après l'API de {url}{Colors.RESET}")
			return last_version
		except IndexError as e:
			return "Error parsing the version: the expected format was not found."
	except Exception as e:
		return f"An error occurred: {e}"
