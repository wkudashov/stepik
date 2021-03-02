import xlrd

product_tab = xlrd.open_workbook('trekking2.xlsx')
product_sheet = product_tab.sheet_by_index(0)
ration_sheet = product_tab.sheet_by_index(1)

products = {}
ration = {}

for row in range(1, product_sheet.nrows):
    products[product_sheet.row_values(row)[0]] = product_sheet.row_values(row)[1:]

for row in range(1, ration_sheet.nrows):
    if ration_sheet.row_values(row)[0] not in ration.keys():
        ration[ration_sheet.row_values(row)[0]] = [ration_sheet.row_values(row)[1]]
    else:
        ration[ration_sheet.row_values(row)[0]][0] += ration_sheet.row_values(row)[1]

for ration_item in ration.keys():
    for product in products[ration_item]:
        if product != '':
            ration[ration_item].append(product*ration[ration_item][0]/100)
        else:
            ration[ration_item].append(0)

sum_cal = int(sum(i[1] for i in ration.values()))
sum_prot = int(sum(i[2] for i in ration.values()))
sum_fat = int(sum(i[3] for i in ration.values()))
sum_carb = int(sum(i[4] for i in ration.values()))

print(sum_cal, sum_prot, sum_fat, sum_carb)