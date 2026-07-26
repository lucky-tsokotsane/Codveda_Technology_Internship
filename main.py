from bs4 import BeautifulSoup
import requests, pandas as pd, csv

web_soup = BeautifulSoup(requests.get('https://lyai3h2tol4i4.ok.kimi.link/').content, 'html.parser')
shoes = web_soup.find_all('div', class_='product-card')

with open('stored_data.csv', 'wt', newline='') as csvfile:
    for shoe in shoes:
        shoe_name = shoe.find('h3', class_='product-name').text
        shoe_color = shoe.find('p', class_='product-color').text
        shoe_price = shoe.find('p', class_='product-price').text

        csv.writer(csvfile).writerow([shoe_name, shoe_color, shoe_price])