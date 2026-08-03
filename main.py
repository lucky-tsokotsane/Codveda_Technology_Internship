from bs4 import BeautifulSoup
import requests, pandas as pd

def webscrape(base_site, target_site):
    data_frame = pd.DataFrame(columns=['SHIRT NAME', 'SHIRT PRICE', 'SHIRT SPECIAL', 'SHIRT DEAL'])
    next_page = True

    while next_page:
        site = requests.get(url=target_site)
        soup = BeautifulSoup(site.content, 'html.parser')
        cards = soup.find_all('div', class_='gtm-product-tile css-18icsov')

        for card in cards:
            shirt_row_name = Null(card.find('p', class_='chakra-text'))
            shirt_row_price = Null(card.find('p', class_='css-1wlfx5v'))
            shirt_row_special = Null(card.find('div', class_='css-dx5xao'))
            shirt_row_deal = Null(card.find('div', class_='css-qczfus'))

            data_frame.loc[len(data_frame)] = [shirt_row_name, shirt_row_price, shirt_row_special, shirt_row_deal]
            data_frame.to_csv(r'stored_data.csv', index=False)

        if site.url != base_site+soup.find_all('a', class_='css-fko5fo')[1].attrs['href']:
            target_site = base_site+soup.find_all('a', class_='css-fko5fo')[1].attrs['href']
        else:
            next_page = False


def Null(html_tag):
    if html_tag is None:
        return 'NO VALUE'
    else:
        return html_tag.text.strip()


if __name__ == '__main__':
    webscrape(base_site='https://www.oldkhaki.co.za', target_site='https://www.oldkhaki.co.za/c/mens-tops-tshirts?offset=0')