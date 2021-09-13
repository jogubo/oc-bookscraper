**Note:** This project is realized during my training at OpenClassrooms.

# BookScraper

Ce script permet de récupérer les données des du site [Books to Scrape](https://books.toscrape.com/) dans un fichier csv.

## Utilisation

Depuis la racine du projet, créer un environement virtuel :

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Lancer ensuite le scrip avec la commande `python bookscraper/bookscraper.py`
Les données sont enregistrées dans un sous dossier `data` du répertoire courant.
