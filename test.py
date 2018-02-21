import requests
from bs4 import BeautifulSoup
import json
import io
import pandas as pd

url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=laptop"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

names = []
companies = []
prices = []
in_stocks = []
more_buying_choices = []

titles1 = soup.find_all('div', class_='a-fixed-left-grid')
lent = len(titles1)
print (lent)
count = 0
for title in titles1:
    try:
        # The name
        name = title.h2.text
        names.append(name)
        print(name)
    except:
        pass

    try:
		# The company manufactured by
		company = title.find_all(
		    'span', class_='a-size-small a-color-secondary')[1].text
		companies.append(company)
		print(company)
	except:
		pass

	try:
		# Price
		price = title.find_all('span', class_='sx-price-whole')[0].text
		prices.append(price)
		print(price)
	except:
		pass

	try:
		# in stock
		stock = title.find_all('span', class_='a-size-small a-color-price')[0].text
		in_stocks.append(stock)
		print(stock)
	except:
		pass

	try:
		# more buying options
		more_buying_choice = title.find_all('span', class_='a-size-base a-color-base')[0].text
		more_buying_choices.append(more_buying_choice)
		print(more_buying_choice)
	except:
		pass

	print("????????????????????????????????")
