from datetime import datetime

from read_inventory_csv import read_inventory_csv
from grab_images import grab_images
from write_latex import write_latex
from grab_site_sku_images import grab_site_sku_images


def main():
    inventory = read_inventory_csv()

    use_personal_images = False
    if use_personal_images:
        grab_images(inventory)
    else:
        grab_site_sku_images(inventory)

    #sort inventory by date
    inventory_commision = [item for item in inventory if item.sale_date is not '']
    inventory_commision.sort(key=lambda item: datetime.strptime(item.sale_date, "%m/%d/%Y"), reverse=True)

    write_latex(inventory_commision)


if __name__ == "__main__":

    main()
