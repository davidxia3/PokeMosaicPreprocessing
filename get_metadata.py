from PIL import Image
import numpy as np
import os
import json

folder = 'resized_images'

images = os.listdir(folder)


for image_path in images:

    image = Image.open(os.path.join(folder,image_path))

    image = image.convert('RGB')

    image_array = np.array(image)

    mean_rgb = np.mean(image_array, axis=(0, 1))
    std_dev_rgb = np.std(image_array, axis=(0, 1))

    image_data = {
        'id': image_path.split('.')[0],
        'mean_r': mean_rgb[0], 
        'mean_g': mean_rgb[1],
        'mean_b': mean_rgb[2],
        'std_r': std_dev_rgb[0],
        'std_g': std_dev_rgb[1],
        'std_b': std_dev_rgb[2]
    }

    with open('image_metadata/metadata_' + image_path.split('.')[0] + '.json' , 'w') as json_file:
        json.dump(image_data, json_file, indent=4)
