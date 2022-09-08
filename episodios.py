import requests

from collections import Counter


base_url = 'https://rickandmortyapi.com/api'

episodios = []

count = 49

while True:
    episodio = requests.get(f'{base_url}/episode/{count}')
    episodio = episodio.json()

    print(episodio['name'])
    episodios.append(episodio['name'])
    count += 1

episodios