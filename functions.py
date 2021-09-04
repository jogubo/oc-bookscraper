import requests
from bs4 import BeautifulSoup


def product_scrap(url):
    """Scrap data from a product"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("div", class_="product_main").find("h1")
    description = soup.find("article", class_="product_page").find(
            "p", recursive=False)
    img = soup.find("div", class_="thumbnail").find("img")
    img = img['src'].replace('../../', '')
    img_url = "https://books.toscrape.com/" + img
    product_info = soup.find("table", class_="table-striped").find_all("td")
    upc = product_info[0].string
    price_et = product_info[2].string
    price_it = product_info[3].string
    stock = product_info[5].string
    product_list = [
            title.string,
            description.string,
            price_et,
            price_it,
            upc,
            stock,
            img_url,
            url
            ]
    return product_list
