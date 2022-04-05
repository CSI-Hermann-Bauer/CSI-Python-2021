import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67775/pg67775.txt")
print(res.text[:300])
