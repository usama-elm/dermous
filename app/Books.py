import os
import ebooklib
from ebooklib import epub
from collections import defaultdict
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Words import Word

class Book:
    def __init__(self, bookPath: str, lang: str = None):
        self.bookPath = bookPath
        self.lang = lang

    def BookToText(self):
        book = epub.read_epub(self.bookPath)
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                try:
                    content = item.get_content().decode('utf-8')
                    return content
                except Exception as e:
                    print(f"Error decoding item content for {self.bookPath}: {e}")
    
    def BookToWords(self):
        tokenizedText = word_tokenize(self.BookToText(), language=self.lang)
        return [token.lower() for token in tokenizedText if token.isalpha()]
    
class BookCollection:
    def __init__(self, bookCollectionPath: str, shLang: str = None, lang: str = None):
        self.bookCollectionPath = bookCollectionPath
        self.lang = lang
        self.shLang = shLang

    def CollectionToBooks(self):
        return [Book(bookPath=os.path.join(self.bookCollectionPath, bookPath), lang=self.lang) for bookPath in os.listdir(self.bookCollectionPath) if bookPath.endswith(".epub")] 
    
    def CollectionToWordList(self):
        CollectionOfBooks = self.CollectionToBooks()
        WordList = list()
        for book in CollectionOfBooks:
            WordList.extend(book.BookToWords())
        return WordList
    
    def _load_processed_books(self):
        processed_books_path = os.path.join(self.bookCollectionPath, 'processed_books.txt')
        if os.path.exists(processed_books_path):
            with open(processed_books_path, 'r') as file:
                return set(file.read().splitlines())
        return set()

    def _save_processed_books(self):
        processed_books_path = os.path.join(self.bookCollectionPath, 'processed_books.txt')
        with open(processed_books_path, 'w') as file:
            for book in self.processed_books:
                file.write(f"{book}\n")

    def CollectionWordsExport(self, outputPath: str):
        outputFile = os.path.join(outputPath, "clean.csv")
        fileExists = os.path.isfile(outputFile)
        CollectionOfBooks = self.CollectionToBooks()
        
        for book in CollectionOfBooks:
            print(f"You are on book {book.bookPath}")
            with open(outputFile, 'a+', newline='', encoding='utf-8') as csvExport:
                fieldnames = ['word']
                writer = csv.DictWriter(csvExport, fieldnames=fieldnames)
                
                if not fileExists:
                    writer.writeheader()  # Write header only if file does not exist
                    fileExists = True  # Prevent header from being written again
                
                bookWords = book.BookToWords()
                for word in bookWords:
                    if Word(word, Lang=self.shLang).IsLanguageWord():
                        writer.writerow({'word': word})  # Assuming 'count' should be included but it's missing in the loop
                        print(f"Word: {word}")