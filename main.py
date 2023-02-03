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

    write_latex(inventory)


if __name__ == "__main__":

    main()
