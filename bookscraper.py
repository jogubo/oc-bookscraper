import functions as fct

category_url = fct.select_cat()
page_url = category_url
page_nb = 1

while page_url is not None:
    page_url = fct.page(category_url, page_nb)
    books = fct.books_links(page_url)
    i = 0
    for book in books:
        fct.product_infos(books[i])
        i += 1
    page_nb += 1
