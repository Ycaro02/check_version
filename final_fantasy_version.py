import requests
from bs4 import BeautifulSoup

def get_latest_ffxiv_updates(limit=10):
	url = 'https://fr.finalfantasyxiv.com/lodestone/news/category/3'

	response = requests.get(url)
	
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')

		# Find all elements with the class 'news__list--title'
		update_elems = soup.find_all('p', class_='news__list--title')

		updates = []
		for elem in update_elems[:limit]:
			update_title = elem.text.strip()
			# Check if title contains 'FINAL FANTASY XIV' and not 'Companion' 
			if update_title.find('FINAL FANTASY XIV') != -1 & update_title.find('Companion') == -1:
				updates.append(update_title)

		return updates
	else:
		print(f"Erreur lors de la requête : {response.status_code}")

	return None


def get_ff_last():
	latest_updates = get_latest_ffxiv_updates(20)
	if latest_updates:
		print("Les 10 dernières mises à jour de FINAL FANTASY XIV :")
		for idx, update in enumerate(latest_updates, start=1):
			print(f"{idx}. {update}")
