import zipfile, os, tempfile, requests


lst = []
d = os.getcwd()

with tempfile.TemporaryDirectory() as directory:
    os.chdir(directory)

    with open('tmp.zip', "wb") as tmp:
        tmp.write(requests.get("https://stepik.org/media/attachments/lesson/24465/main.zip").content)

    with zipfile.ZipFile("tmp.zip", 'r') as tmp:
        tmp.extractall()

    for current_dir, subdir, files in os.walk('main'):
        if any(map(lambda f: f.endswith('.py'), files)):
            lst.append(current_dir)
    os.chdir(d)

lst.sort()

with open('result.txt', 'w') as _ouf:
    for s in lst:
        _ouf.writelines(s + '\n')
