import pandas as pd
import requests
import os

def extract_german_books(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file, usecols=['Text#', 'Title', 'Issued', 'Language'])
    # Filter German books
    german_books = data[data['Language'] == 'de']
    # Get a list of book IDs
    book_ids = german_books['Text#'].tolist()
    return book_ids


def download_epub(book_id):
    epub_filename = f'book_{book_id}.epub'

    # Check if the ePub file already exists before downloading it
    if os.path.exists(epub_filename):
        print(f"Book {book_id} already exists. Skipping download.")
        return

    url = f'https://www.gutenberg.org/ebooks/{book_id}.epub.images'
    response = requests.get(url)

    if response.status_code == 200:
        with open(epub_filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Error downloading book {book_id}: {response.status_code}")

os.makedirs('epub_files', exist_ok=True)
os.chdir('epub_files')
german_book_ids = extract_german_books('../pg_catalog.csv')

for book_id in german_book_ids:
    download_epub(book_id)
