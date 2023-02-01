from Inventory_Item import Inventory_Item


def write_latex(all_inventory: [Inventory_Item]) -> bool:

    with open('latex/inventory.tex', 'w') as f:
        f.write('\\documentclass{report}\n')
        f.write('\\usepackage[margin=0.5in]{geometry}\n')
        f.write('\\usepackage{multirow}\n')
        f.write('\\usepackage{graphicx}\n')
        f.write('\\begin{document}\n')

        item_counter = 0
        for item in all_inventory:
            item_counter += 1
            f.write('\n')
            f.write('\\begin{table}[]\n')
            f.write('\\begin{tabular}{llllllll}\n')
            f.write('\\multicolumn{8}{l}{' + item.name + '}\\\\ \n')
            f.write('\\multirow{3}{*}{\\includegraphics[width=3cm, height=3cm]{./../' + item.image_location + '}} & Price & Commission Rate & Commission Amount & Recieved & Sale \\\\ \n')
            f.write(' & ' + item.price + ' & ' + item.commission_rate + ' & ' + item.commission_amount + ' & ' + item.received_date + ' & ' + item.sale_date + ' \\\\ \n')
            f.write(' & \\multicolumn{3}{l}{\\multirow{2}{*}{' + "description here" + '}} &  \\\\ \n') #item.description
            f.write('\\end{tabular}\n')
            f.write('\\end{table}\n')

            if item_counter is 5:
                f.write('\n\\clearpage\n')
                item_counter = 0

        f.write('\\end{document}\n')
    return True

