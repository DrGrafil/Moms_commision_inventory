import os
import urllib.request
from urllib.parse import urlparse
from pathlib import Path
from Inventory_Item import Inventory_Item


def grab_site_sku_images(all_inventory: [Inventory_Item]) -> bool:
    for item in all_inventory:
        file_name = item.sku + "_1_product.jpg"
        if item.sku is '':
            print("No Image")
            item.image_location = 'images_sku/no_image.jpg'
        else:
            print("File: " + file_name)
            image_path = 'images_sku/' + file_name

            item.image_location = image_path

            if os.path.exists(image_path):
                print("File :" + image_path + " already exists")
            else:
                "https://product-images.therealreal.com/BRU218318_1_product.jpg"
                url_path = "https://product-images.therealreal.com/" + file_name
                urllib.request.urlretrieve(url_path, image_path)
                print("File savepath:" + image_path)

    return True
