import csv
import tempfile
import requests

result = {}

with tempfile.TemporaryFile(mode='w+') as table:
    print('Getting a file from Stepik.org')
    table.write(requests.get("https://stepik.org/media/attachments/lesson/24473/Crimes.csv").text)
    table.seek(0)
    print('Done!')
    data = csv.DictReader(table)
    for row in data:
        if '2015' in row['Date']:
            if row['Primary Type'] in result.keys():
                result[row['Primary Type']] += 1
            else:
                result[row['Primary Type']] = 1

print('\nFirst Primary Type is:', max(result, key=result.get))
