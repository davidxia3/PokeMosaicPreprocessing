import os
import requests
import json

with open('cards.json', 'r') as file:
    cards = json.load(file)

folder_path = 'images'


for card in cards:
    url = cards[card]["image"]

    set = url.split('/')[-2]
    number = url.split('/')[-1].split('_')[0]
    filename = set + '-' + number + '.png'
    file_path = os.path.join(folder_path, filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print('error:' + file_path)
