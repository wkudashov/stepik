import xlrd

product_tab = xlrd.open_workbook('trekking1.xlsx')
product_sheet = product_tab.sheet_by_index(0)

calories = {}

for row in range(1, product_sheet.nrows):
    if product_sheet.row_values(row)[1] not in calories.keys():
        calories[product_sheet.row_values(row)[1]] = [product_sheet.row_values(row)[0]]
    else:
        calories[product_sheet.row_values(row)[1]].append(product_sheet.row_values(row)[0])

with open('result.txt', 'w') as ouf:
    for i in sorted(calories.keys(), reverse=True):
        for j in sorted(calories[i]):
            ouf.write(j+'\n')
