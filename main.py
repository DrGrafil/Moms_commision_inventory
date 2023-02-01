


def main():
    inventory = read_inventory_csv()
    grab_images(inventory.image_list)

    write_latex(inventory)




if __name__ == "__main__":

    main()
