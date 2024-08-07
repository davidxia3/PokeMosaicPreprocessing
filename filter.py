import os
import json
import shutil

with open("cards.json", "r") as file:
    cards = json.load(file)

filtered_cards = {}

for card in cards:
    if cards[card]["supertype"] != "Energy":
        try:
            shutil.copy("resized_images/"+cards[card]["id"] + ".png", "filtered_images/" + cards[card]["id"] + ".png")
            shutil.copy("image_metadata/metadata_"+cards[card]["id"] + ".json", "filtered_metadata/metadata_" + cards[card]["id"] + ".json")
        except Exception as e:
            print(e)
        

