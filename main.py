import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b99b6c3a5c0b1ea642e3507bc3efb7c5"
HEADER = {"Content-type": "application/json", "trainer_token": TOKEN}

body_pokemons = {"name": "TEST", "photo_id": -1}

body_put_pokemons = {"pokemon_id": "202328", "name": "Поменяшка", "photo_id": 25}

body_add_pokeball = {"pokemon_id": "202328"}

'''Create pokemon'''
response = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=body_pokemons)
print(response.text)

'''Change pokemon'''
response = requests.put(url=f"{URL}/pokemons", headers=HEADER, json=body_put_pokemons)
print(response.text)

'''Catch pokemon in pokeball'''
response = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_add_pokeball
)
print(response.text)
