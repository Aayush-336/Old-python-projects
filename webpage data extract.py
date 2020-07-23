import requests
import json
para = {'q':'"Hello Google"'}
d={'rel_rhy':'funny'}
page = requests.get("https://www.google.com/search",params=para).url
print(page)
x=requests.get("https://api.datamuse.com/words",params=d).json()
print(x[0])






