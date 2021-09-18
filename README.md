**Note:** This project is realized during my training at OpenClassrooms.

# BookScraper

Ce script permet de récupérer les données du site [Books to Scrape](https://books.toscrape.com/) dans un fichier csv.

## Utilisation

Depuis la racine du projet, créer un environement virtuel et lancer le script:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python bookscraper.py
```

Les données sont enregistrées dans un sous dossier `bookscraper-data` du répertoire courant.
