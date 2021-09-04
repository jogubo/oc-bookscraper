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
    img = img['src'].replace('../../', 'https://books.toscrape.com/')
    product_info = soup.find("table", class_="table-striped").find_all("td")
    upc = product_info[0].string
    price_et = product_info[2].string
    price_it = product_info[3].string
    stock = product_info[5].string
    rating = str(soup.find("p", class_="star-rating"))
    if ("One") in rating:
        rating = "1/5"
    elif ("Two") in rating:
        rating = "2/5"
    elif ("Three") in rating:
        rating = "3/5"
    elif ("Four") in rating:
        rating = "4/5"
    elif ("Five") in rating:
        rating = "5/5"
    else:
        rating = None
    product_list = [
            title.string,
            description.string,
            rating,
            price_et,
            price_it,
            upc,
            stock,
            img,
            url
            ]
    return product_list