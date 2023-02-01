import csv
from Inventory_Item import Inventory_Item



def read_inventory_csv() ->[Inventory_Item]:
    all_inventory:[Inventory_Item] = []
    with open('inventory.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                new_item = Inventory_Item()

                new_item.sku = row[0]
                new_item.vendor_sku = row[1]
                new_item.name = row[2]
                new_item.price = row[3]
                new_item.status = row[4]
                new_item.image_url = row[5]
                new_item.description = row[6]
                new_item.commission_rate = row[7]
                new_item.commission_amount = row[8]
                new_item.received_date = row[9]
                new_item.sale_date = row[10]

                new_item.image_location = None

                all_inventory.append(new_item)
                line_count += 1
        print(f'Processed {line_count} lines.')

    return all_inventory