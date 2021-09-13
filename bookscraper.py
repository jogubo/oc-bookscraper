import os
import requests
import time
import csv
import urllib.request
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
    try:
        description = description.string
    except AttributeError:
        description = ""
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
            description,
            rating,
            price_et,
            price_it,
            upc,
            stock,
            img,
            url
            ]
    print(product_list[0])
    writecsv(product_list)
    img_name = product_list[6] + ".jpg"
    urllib.request.urlretrieve(product_list[8], "bookscraper-data/img/" + img_name)
    return product_list


def writecsv(data):
    with open("bookscraper-data/bookscraper.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(data)


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
    categories = soup.find("ul", class_="nav").find("li").find_all("a")
    cat_list, i = [], 0
    for li in categories:
        cat = li.string.strip().replace("\n", "")
        link = main_url + li['href']
        if i == 0:
            cat = ["All", link]
        else:
            cat = [cat, link]
        i += 1
        cat_list.append(cat)
    return cat_list


def select_cat():
    """View and select category"""
    cat_list = list_categories()
    while True:
        i = 0
        for cat_nb in cat_list:
            if i < 10:
                print(" " + str(i) + " - " +cat_nb[0])
            else:
                print(str(i) + " - " + cat_nb[0])
            i += 1
        select = input("\nEntrez le numéro de la catégorie "
                       "dont vous souhaitez recupérer les données : ")
        try:
            select = int(select)
            if select >= 0 and select < i:
                break
            else:
                print("Pas de catégorie correspondante\n")
                continue
        except ValueError:
            print("Commande incorrecte\n")
            continue
    cat = cat_list[select]
    print("\n[RECUPÉRATION DES DONNÉES DE "
          "LA CATÉGORIE '" + cat[0].upper() + "']\n")
    return cat[1]


def books_links(page_url):
    """Retrieves books urls"""
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find("ol", class_="row").find_all("a")
    books, i = [], 0
    for href in links:
        link = links[i]['href'].replace("../../", "")
        link = main_url + "catalogue/" + link.replace("../", "")
        if i % 2 == 0:
            books.append(link)
            i += 1
        else:
            i += 1
    return books


def page(url, p):
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



print("\n[BOOKSCRAPER]\n")
category_url = select_cat()
page_url = category_url
page_nb = 1
count = 0
if os.path.exists('bookscraper-data'):
    if os.path.exists('bookscraper-data/img'):
        pass
    else:
        os.mkdir('bookscraper-data/img')
else:
    os.mkdir('bookscraper-data')
    os.mkdir('bookscraper-data/img')
while page_url is not None:
    books = books_links(page_url)
    for book in books:
        product_infos(book)
        count += 1
    page_url = page(category_url, page_nb)
    page_nb += 1
print("\n[TERMINÉ, " + str(count) + " LIVRES "
      "IMPORTÉS AVEC SUCCÈS]\n")
