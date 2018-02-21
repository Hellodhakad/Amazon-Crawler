import requests
from bs4 import BeautifulSoup
import json
import io
'''for making available for python 2 and 3'''

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

find_product = raw_input('Enter Keyword to find on amazon')
url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + find_product + "&rh=i%3Aaps%2Ck%3A" + find_product
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

for i in range(1, 20):
    if i > 1:
        url = "https://www.amazon.com/s/ref=sr_pg_3?fst=as%3Aon&rh=k%3A" + find_product + "%2Cn%3A172282&page=" + str(
            i) + "&keywords=" + find_product + "&ie=UTF8&qid=1518357568"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    titles = soup.find_all("a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})

    data = []
    for title_one in titles:
        title = {"Title": title_one.string}
        data.append(title)
    jsonData = json.dumps(data)
    with open('data.json', 'w') as fs:
        json.dump(jsonData, fs)
