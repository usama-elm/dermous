import os
import ebooklib
from ebooklib import epub
from collections import defaultdict
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_epub(epub_file):
    book = epub.read_epub(epub_file)
    text = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            try:
                content = item.get_content().decode('utf-8')
                text += content
            except Exception as e:
                print(f"Error decoding item content for {epub_file}: {e}")
    return text

def get_words(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Filter tokens to keep only words (removes XML tags, punctuation, etc.)
    words = [token.lower() for token in tokens if token.isalpha()]

    return words

def create_word_database(epub_directory):
    word_database = defaultdict(int)

    for epub_file in os.listdir(epub_directory):
        if epub_file.endswith(".epub"):
            file_path = os.path.join(epub_directory, epub_file)
            text = extract_text_from_epub(file_path)
            words = get_words(text)

            for word in words:
                word_database[word.lower()] += 1

    return word_database

def write_word_database_to_csv(word_database, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, count in word_database.items():
            writer.writerow({'word': word, 'count': count})

    print(f"CSV file with unique words and counts has been created: {output_file}")

epub_directory = "/ryuu/german_books"
word_database = create_word_database(epub_directory)

output_file = 'unique_words.csv'
write_word_database_to_csv(word_database, output_file)
