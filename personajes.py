import requests

from collections import Counter


base_url = 'https://rickandmortyapi.com/api'

especies = []

for i in range(1, 827):
    personaje = requests.get(f'{base_url}/character/{i}')
    personaje = personaje.json()
    especies.append(personaje['species'])

print(Counter(especies))
