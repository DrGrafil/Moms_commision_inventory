import urllib.request
from Inventory_Item import Inventory_Item


def grab_images(all_inventory: [Inventory_Item]) -> bool:
    for item in all_inventory:
        print(item.image_url)
        #urllib.request.urlretrieve()

    return True
