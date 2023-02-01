from read_inventory_csv import read_inventory_csv
from grab_images import grab_images
from write_latex import write_latex

def main():
    inventory = read_inventory_csv()
    grab_images(inventory)

    write_latex(inventory)


if __name__ == "__main__":

    main()
