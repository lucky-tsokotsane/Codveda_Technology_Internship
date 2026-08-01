from bs4 import BeautifulSoup
import requests, pandas as pd

def webscrape(url):
    site = requests.get(url=url)
    soup = BeautifulSoup(site.content, 'html.parser')

    cards = soup.find_all('div', class_='gtm-product-tile css-18icsov')
    data_frame = pd.DataFrame(columns=['SHIRT NAME', 'SHIRT PRICE', 'SHIRT SPECIAL', 'SHIRT DEAL'])

    for card in cards:
        shirt_row_name = Null(card.find('p', class_='chakra-text'))
        shirt_row_price = Null(card.find('p', class_='css-1wlfx5v'))
        shirt_row_special = Null(card.find('div', class_='css-dx5xao'))
        shirt_row_deal = Null(card.find('div', class_='css-qczfus'))

        data_frame.loc[len(data_frame)] = [shirt_row_name, shirt_row_price, shirt_row_special, shirt_row_deal]
        data_frame.to_csv(r'stored_data.csv', index=False)


def Null(finder):
    if finder is None:
        return 'NO VALUE'
    else:
        return finder.text.strip()


if __name__ == '__main__':
    webscrape(url='https://www.oldkhaki.co.za/c/mens-tops-tshirts')