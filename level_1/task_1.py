from bs4 import BeautifulSoup
import requests, pandas as pd

def webscrape(target_site="https://www.truworths.co.za/category/men"):
    dataFrame = pd.DataFrame(columns=["TITLE", "BRAND", "PRICE", "IMAGE_URL"])

    for page_no in range(1, int(BeautifulSoup(requests.get(url=target_site).content, features="html.parser").find_all(name="a", class_="StandardPagination__PageIndicator")[-1].text) + 1):
        site = requests.get(url=f"https://www.truworths.co.za/category/men?page={page_no}")
        soup = BeautifulSoup(site.content, features="html.parser")
        cards = soup.find_all(name="div", class_="single-product-tile-wrapper")

        for card in cards:
            product_image_url = card.find(name="img", class_="lazy").attrs['src']
            product_brand = card.find(name="p", class_="product-tile-brand").text
            product_name = card.find(name="p", class_="product-tile-title").text
            product_price = card.find(name="span", class_="product-tile-price").text

            dataFrame.loc[len(dataFrame)] = [product_name, product_brand, product_price, product_image_url]
            dataFrame.to_csv(path_or_buf="stored_data.csv", index=False)

if __name__ == '__main__':
    webscrape()