import os
import urllib.request
from urllib.parse import urlparse
from pathlib import Path
from Inventory_Item import Inventory_Item


def grab_images(all_inventory: [Inventory_Item]) -> bool:
    for item in all_inventory:
        file_name = os.path.splitext(os.path.basename(item.image_url))
        if file_name[0] is '':
            print("No Image")
            item.image_location = 'images/no_image.jpg'
        else:
            print("File:" + file_name[0] + " ext:" + file_name[1])
            image_path = None
            if file_name[1] is '':
                image_path = 'images/' + file_name[0] + '.jpg'
            else:
                image_path = 'images/' + file_name[0] + file_name[1]

            item.image_location = image_path

            if os.path.exists(image_path):
                print("File :" + image_path + " already exists")
            else:
                urllib.request.urlretrieve(item.image_url, image_path)
                print("File savepath:" + image_path)

    return True
