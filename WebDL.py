import requests
res = requests.get('#link goes here')
res.raise_for_status()
playFile = open('#Name your file here.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
