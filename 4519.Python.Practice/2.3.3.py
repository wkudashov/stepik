import xlrd

product_tab = xlrd.open_workbook('trekking3.xlsx')
product_sheet = product_tab.sheet_by_index(0)
ration_sheet = product_tab.sheet_by_index(1)

products = {}
ration = {}
result = {}

for row in range(1, product_sheet.nrows):
    products[product_sheet.row_values(row)[0]] = product_sheet.row_values(row)[1:]

for row in range(1, ration_sheet.nrows):
    if ration_sheet.row_values(row)[1] not in ration.keys():
        ration[ration_sheet.row_values(row)[1]] = {int(ration_sheet.row_values(row)[0]): [ration_sheet.row_values(row)[2]]}
    else:
        if int(ration_sheet.row_values(row)[0]) not in ration[ration_sheet.row_values(row)[1]].keys():
            ration[ration_sheet.row_values(row)[1]][int(ration_sheet.row_values(row)[0])] = [ration_sheet.row_values(row)[2]]
        else:
            ration[ration_sheet.row_values(row)[1]][int(ration_sheet.row_values(row)[0])][0] += ration_sheet.row_values(row)[2]

for ration_item in ration.keys():
    for product in products[ration_item]:
        if product != '':
            for ration_day in ration[ration_item].keys():
                ration[ration_item][ration_day].append(product*ration[ration_item][ration_day][0]/100)
        else:
            for ration_day in ration[ration_item].keys():
                ration[ration_item][ration_day].append(0)

for ration_item in ration.keys():
    for ration_day in ration[ration_item].keys():
        if ration_day not in result.keys():
            result[ration_day] = ration[ration_item][ration_day][1:]
        else:
            result[ration_day] = list(map(lambda x, y: x + y, result[ration_day], ration[ration_item][ration_day][1:]))

for i in sorted(result.keys()):
    for j in result[i]:
        print(int(j), end=' ')
    print()

