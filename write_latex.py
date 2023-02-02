from Inventory_Item import Inventory_Item


def write_latex(all_inventory: [Inventory_Item]) -> bool:

    # price, commision amount, price-commision, item count
    total_per_year = {
        "16": (0, 0, 0, 0),
        "17": (0, 0, 0, 0),
        "18": (0, 0, 0, 0),
        "19": (0, 0, 0, 0),
        "20": (0, 0, 0, 0),
        "21": (0, 0, 0, 0),
        "22": (0, 0, 0, 0),
        "23": (0, 0, 0, 0)
    }


    with open('latex/inventory.tex', 'w') as f:
        f.write('\\documentclass{report}\n')
        f.write('\\usepackage[margin=0.5in]{geometry}\n')
        f.write('\\usepackage{multirow}\n')
        f.write('\\usepackage{graphicx}\n')
        f.write('\\usepackage{fancyhdr}\n')

        f.write('\\pagestyle{fancy}\n')
        f.write('\\fancyhf{}\n')
        f.write('\\fancyfoot[R]{\\thepage}\n')

        f.write('\\setlength{\\voffset}{-0.75in}\n')

        f.write('\\date{\\today}\n')
        f.write('\\author{Elliot M Grafil}\n')
        f.write('\\title{Summary of The Real Real Sales}\n')

        f.write('\\begin{document}\n')
        f.write('\\maketitle\n')

        item_counter = 0
        for item in all_inventory:
            item_counter += 1
            f.write('\n')
            f.write('\\begin{table}[]\n')
            f.write('\\begin{tabular}{llllllll}\n')
            f.write('\\multicolumn{8}{l}{\\textbf{' + item.name.replace("&", "\\&") + '}}\\\\ \n')
            f.write('\\hline \\\\\n')
            f.write('\\multirow{3}{*}{\\includegraphics[width=3.5cm, height=3.5cm]{./../' + item.image_location + '}} & Price & Commission Rate & Commission Amount & Recieved & Sale \\\\ \n')
            f.write(' & ' + item.price + ' & ' + item.commission_rate + ' & ' + item.commission_amount + ' & ' + item.received_date + ' & ' + item.sale_date + ' \\\\ \n')
            f.write(' & \\multicolumn{7}{l}{\\multirow{2}{*}{\\parbox[t]{15cm}{\\small ' + item.description.replace("&", "\\&") + '}}} \\\\ \n')
            f.write('\\end{tabular}\n')
            f.write('\\end{table}\n')

            if item_counter is 5:
                f.write('\n\\clearpage\n')
                item_counter = 0

            if item.sale_date is not '':
                year = item.sale_date.rsplit('/', 1)[-1]
                year = year[-2:]
                data = total_per_year[str(year)]
                a = float(data[0])+float(item.price)
                b = 0
                c = 0
                if item.commission_amount is not '':
                    b = float(data[1])+float(item.commission_amount)
                    c = float(data[2])+float(item.price)-float(item.commission_amount)
                else:
                    b = float(data[1])
                    c = float(data[2]) + float(item.price)

                d = float(data[3])+1
                total_per_year[str(year)] = (a, b, c, d)

        f.write('\n\\clearpage\n')
        f.write('\n')
        f.write('\\begin{table}[]\n')
        f.write('\\centering\n')
        f.write('\\begin{tabular}{|lllll|}\n')
        f.write('\\hline \n')
        f.write('Year & Price & Commission Amount & Price-Commission Amount & Item Count \\\\ \n')
        f.write('\\hline \n')

        final_tally = (0, 0, 0, 0)
        for year_total in total_per_year.items():
            total = year_total[1]
            f.write(str(year_total[0]) + ' & \\$' + str(round(total[0], 2)) + ' & \\$' + str(round(total[1], 2)) + ' & \\$' + str(round(total[2], 2)) + ' & ' + str(round(total[3], 2)) + ' \\\\ \n')
            final_tally = (final_tally[0]+total[0], final_tally[1]+total[1], final_tally[2]+total[2], final_tally[3]+total[3])

        f.write('\\hline  \n')
        f.write('Total: & \\$' + str(round(final_tally[0], 2)) + ' & \\$' + str(round(final_tally[1], 2)) + ' & \\$' + str(round(final_tally[2], 2)) + ' & ' + str(round(final_tally[3], 2)) + ' \\\\ \n')
        f.write('\\hline  \n')
        f.write('\\end{tabular}\n')
        f.write('\\end{table}\n')
        f.write('\\end{document}\n')
    return True

