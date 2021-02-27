import xlrd
from statistics import median
from statistics import mean


salary_tab = xlrd.open_workbook('salaries.xlsx')
salary_sheet = salary_tab.sheet_by_index(0)

medians = {}
avgs = {}

for row in range(1, salary_sheet.nrows):
    medians[median(salary_sheet.row_values(row)[1:])] = salary_sheet.row_values(row)[0]
region_max_median = medians[max(medians.keys())]

for col in range(1, salary_sheet.ncols):
    avgs[mean(salary_sheet.col_values(col)[1:])] = salary_sheet.col_values(col)[0]
profession_max_avg = avgs[max(avgs.keys())]

print(region_max_median, profession_max_avg)
