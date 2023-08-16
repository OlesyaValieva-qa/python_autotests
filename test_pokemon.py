import requests
import pytest


def test_status_code_create_pokemon():
    token = '84e8c0677a08f818b98490ba776c1caa' 
    response = requests.post('https://api.pokemonbattle.me:9104/pokemons', headers={'trainer_token': token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
})
    assert response.status_code == 201


def test_trainer_name():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers', params={'trainer_id': 1626})
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['trainer_name'] == 'хопа'
