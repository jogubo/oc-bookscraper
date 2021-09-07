import functions as fct
import os


print("\n[BOOKSCRAPER]\n")
category_url = fct.select_cat()
page_url = category_url
page_nb = 1
count = 0
if os.path.exists('data'):
    if os.path.exists('data/img'):
        pass
    else:
        os.mkdir('data/img')
else:
    os.mkdir('data')
    os.mkdir('data/img')
while page_url is not None:
    books = fct.books_links(page_url)
    i = 0
    for book in books:
        fct.product_infos(books[i])
        i += 1
        count += 1
    page_url = fct.page(category_url, page_nb)
    page_nb += 1
print("\n[TERMINÉ, " + str(count) + " LIVRES "
      "IMPORTÉS AVEC SUCCÈS]\n")
