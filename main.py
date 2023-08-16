import requests

token = '84e8c0677a08f818b98490ba776c1caa' 
url = 'https://api.pokemonbattle.me:9104'   

responce_add_pokemon = requests.post (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "name": "Зая",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
})


response_body = responce_add_pokemon.json()
pokemon_id = response_body['id']

print(responce_add_pokemon.text)


change = requests.put (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id,
    "name": "Зая2",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
})
print(change.text)

add_pokeboll = requests.post (f'{url}/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id
})
print(add_pokeboll.text)