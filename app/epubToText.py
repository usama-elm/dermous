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

class Book:
    def __init__(self, bookPath: str):
        self.bookPath = bookPath
    
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
        tokenizedText = word_tokenize(self.BookToText())
        return [token.lower() for token in tokenizedText if token.isalpha()]
    
class BookCollection:
    def __init__(self, bookCollectionPath: str):
        self.bookCollectionPath = bookCollectionPath

    def CollectionToBooks(self):
        return [Book(os.path.join(self.bookCollectionPath, bookPath)) for bookPath in os.listdir(self.bookCollectionPath) if bookPath.endswith(".epub")] 
    
    def CollectionToWordList(self):
        CollectionOfBooks = self.CollectionToBooks()
        WordList = list()
        for book in CollectionOfBooks:
            WordList.extend(book.BookToWords())
        return WordList
    
    def CollectionWordsExport(self, outputPath: str):
        with open(os.join.path(outputPath, "clean.csv"), 'w', newline='', encoding='utf-8') as csvExport:
            fieldnames = ['word', 'count']
            writer = csv.DictWriter(csvExport, fieldnames=fieldnames)
            WordList = self.CollectionToWordList()
            
            writer.writeheader()
            for word, count in WordList.items():
                writer.writerow({'word': word, 'count': count})