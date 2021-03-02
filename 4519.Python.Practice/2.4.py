import requests
import os
import zipfile
import tempfile
import xlrd

url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
salary = {}
with tempfile.TemporaryDirectory() as tmpdir:
    r = requests.get(url, stream=True)
    with open(os.path.join(tmpdir, 'billing.zip'), 'wb') as fd:
        n = 1
        for chunk in r.iter_content(chunk_size=128):
            print('\r', end='')
            fd.write(chunk)
            print(f'Saved {128*n} bytes', end='')
            n += 1
    print()
    with zipfile.ZipFile(os.path.join(tmpdir, 'billing.zip'), 'r') as billing_zip:
        billing_zip.extractall(os.path.join(tmpdir, 'unzip'))
    for file in billing_zip.namelist():
        bill_tab = xlrd.open_workbook(os.path.join(tmpdir, 'unzip', file))
        bill_sheet = bill_tab.sheet_by_index(0)
        if bill_sheet.cell_value(1, 1) not in salary.keys():
            salary[bill_sheet.cell_value(1, 1)] = bill_sheet.cell_value(1, 3)
        else:
            print(f'Duplicated billing list for {bill_sheet.cell_value(1, 1)}!')
    with open('result.txt', 'w', encoding='utf8') as result:
        result.writelines('\n'.join(f'{key} {int(salary[key])}' for key in sorted(salary.keys())))
print('Writing complete')
