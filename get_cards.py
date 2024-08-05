import requests
import certifi
from pokemontcgsdk import RestClient
import json
from pokemontcgsdk import Card


with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config.get('api_key')


RestClient.configure(api_key) 
def custom_get(url, params=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, params=params, verify=certifi.where())
    return response.json()

RestClient.get = custom_get

cards = Card.all()

card_dict = {}
for card in cards:
    price_normal = None
    price_holo = None
    price_reverse = None
    price_first_holo = None
    price_first_normal = None
    if card.tcgplayer!=None and card.tcgplayer.prices!=None:
        if card.tcgplayer.prices.normal!=None:
            price_normal = card.tcgplayer.prices.normal.market
        if card.tcgplayer.prices.holofoil!=None:
            price_holo = card.tcgplayer.prices.holofoil.market
        if card.tcgplayer.prices.reverseHolofoil!=None:
            price_reverse = card.tcgplayer.prices.reverseHolofoil.market
        if card.tcgplayer.prices.firstEditionHolofoil!=None:
            price_first_holo = card.tcgplayer.prices.firstEditionHolofoil.market
        if card.tcgplayer.prices.firstEditionNormal!=None:
            price_first_normal = card.tcgplayer.prices.firstEditionNormal.market
    individual_dict = {
        'id': card.id,
        'name': card.name,
        'supertype': card.supertype,
        'rarity': card.rarity,
        'image': card.images.large,
        'price_normal': price_normal,
        'price_holo': price_holo,
        'price_reverse': price_reverse,
        'price_first_holo': price_first_holo,
        'price_first_normal': price_first_normal
    }
    card_dict[card.id] = individual_dict


with open('cards.json', 'w') as json_file:   
    json.dump(card_dict, json_file, indent=4)

