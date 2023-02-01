from Inventory_Item import Inventory_Item


def write_latex(all_inventory: [Inventory_Item]) -> bool:

    with open('latex/inventory.tex', 'w') as f:
        f.write('\\documentclass{article}\n')
        f.write('\\usepackage{multirow}\n')
        f.write('\\usepackage{graphicx}\n')
        f.write('\\begin{document}\n')

        for item in all_inventory:
            f.write('\n')
            f.write('\\begin{table}[]\n')
            f.write('\\begin{tabular}{lllll}\n')
            f.write('\\multicolumn{5}{l}{'+ item.name +'}\\\\ \n')
            f.write('\\multirow{3}{*}{\\includegraphics[width=5cm, height=5cm]{./../' + item.image_location +'}} & Price: ' + item.price + ' & Commission Rate: ' + item.commission_rate + ' & Commission Amount: '+ item.commission_amount +' & \\\\ \n')
            f.write('& \\multicolumn{3}{l}{\\multirow{2}{*}{' + "description here" + '}} & Date Recieved: ' + item.received_date + ' \\\\ \n') #item.description
            f.write('& \\multicolumn{3}{l}{} & Date Sale: ' + item.sale_date + '\n')
            f.write('\\end{tabular}\n')
            f.write('\\end{table}\n')

        f.write('\\end{document}\n')
    return True

