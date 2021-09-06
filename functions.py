import requests
import time
from bs4 import BeautifulSoup

main_url = "https://books.toscrape.com/"


def product_infos(url):
    """Scrap data from a product"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("div", class_="product_main").find("h1")
    category = soup.find("ul", class_="breadcrumb").find_all("a")
    category = category[2].string
    description = soup.find("article", class_="product_page").find(
            "p", recursive=False)
    img = soup.find("div", class_="thumbnail").find("img")
    img = img['src'].replace('../../', main_url)
    product_info = soup.find("table", class_="table-striped").find_all("td")
    upc = product_info[0].string
    price_et = product_info[2].string
    price_it = product_info[3].string
    stock = product_info[5].string
    rating = product_rating(str(soup.find("p", class_="star-rating")))
    product_list = [
            title.string,
            category,
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


def product_rating(rating):
    """View rating"""
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
    return rating


def list_categories():
    """Retrieves categories and url on the main page"""
    page = requests.get(main_url)
    soup = BeautifulSoup(page.content, "html.parser")
    all = soup.find("ul", class_="nav").find("a")
    all = {"All": main_url + all['href']}
    categories = soup.find("ul", class_="nav").find("li").find_all("a")
    cat_list, i = [all], 0
    for li in categories:
        cat = categories[i].string.strip().replace("\n", "")
        link = main_url + categories[i]['href']
        cat = {cat: link}
        cat_list.append(cat)
        i += 1
    return cat_list


def select_cat():
    """View and select category"""
    while True:
        cat_list = list_categories()
        i = 0
        for cat_nb in cat_list:
            cat = cat_list[i]
            for key in cat.keys():
                if i < 10:
                    print(" " + str(i) + " - " + key)
                else:
                    print(str(i) + " - " + key)
            i += 1
        select_cat = input("Entrez le numéro de la catégorie "
                           "dont vous souhaitez recupérer les données : ")
        select_cat = int(select_cat)
        if select_cat >= 0 and select_cat < i:
            return select_cat
            break
        else:
            print("Commande incorrecte")
            continue


def books_links(url):
    """Retrieves books urls"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find("ol", class_="row").find_all("a")
    books, i = [], 0
    for href in links:
        link = main_url + links[i]['href']
        books.append(link)
        i += 1
    return books


def pages(url, p):
    """Increment the pages"""
    url = url.replace("index.html", "page-" + str(p) + ".html")
    request = requests.get(url)
    if request.ok:
        return url
    else:
        time.sleep(2)
        if request.ok:
            return url
        else:
            return None
