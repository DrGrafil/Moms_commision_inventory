from Inventory_Item import Inventory_Item


def write_latex(all_inventory: [Inventory_Item]) -> bool:
    for item in all_inventory:
        print(item.image_url)
        #urllib.request.urlretrieve()

    return True

