import chunk
import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67775/pg67775.txt")
playFile = open("Gaudenzia", "wb")
for char in res.text:
    playFile.write(chunk)
playFile.close
