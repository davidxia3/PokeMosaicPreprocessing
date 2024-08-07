import os
from PIL import Image

source_folder = 'images'
destination_folder = 'resized_images'

target_dimension = (245, 342)

target_width, target_height = target_dimension
    
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if filename.lower().endswith('.png'):
        try:
            with Image.open(file_path) as img:
                resized_img = img.resize((target_width, target_height), Image.LANCZOS)
                
                destination_path = os.path.join(destination_folder, filename)
                
                resized_img.save(destination_path)
        except Exception as e:
            print(filename)