import requests
from bs4 import BeautifulSoup


def product_scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find("div", class_="product_main").find("h1")

    description = soup.find("article", class_="product_page").find(
            "p", recursive=False)

    img = soup.find("div", class_="thumbnail").find("img")
    img = img['src'].replace('../../', '')
    img_url = "https://books.toscrape.com/" + img

    product_list = [
            url,
            title.string,
            description.string,
            img_url
            ]

    product_info = soup.find("table", class_="table-striped").find_all("td")
    i = 0
    for tds in product_info:
        if i <= 5 and i != 1 and i != 4:
            product_list.append(product_info[i].string)
            i += 1
        else:
            i += 1

    return product_list
