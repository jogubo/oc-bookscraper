import requests
from bs4 import BeautifulSoup


def product_scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find("div", class_="product_main").find("h1")

    stock = soup.find("p", class_="availability")

    description = soup.find("article", class_="product_page").find(
            "p", recursive=False)

    upc = soup.find("td")

    img = soup.find("div", class_="thumbnail").find("img")
    img = img['src'].replace('../../', '')
    img_url = "https://books.toscrape.com/" + img

    product_list = [
            url,
            title.string,
            stock.string,
            description.string,
            upc.string,
            img_url
            ]

    return product_list
