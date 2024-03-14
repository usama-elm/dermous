import requests
# from config import GuthenbergLink
import os
import csv
from io import StringIO
from dotenv import dotenv_values


class RemoteBookCollection():
    def __init__(self, remoteLink: str):
        self.remoteLink = remoteLink

    def LoadList(self):
        return requests.get(self.remoteLink).content.decode("utf-8")

    def ToDict(self):
        return csv.DictReader(StringIO(self.LoadList()))
    
    def FilerOnLanguage(self, lang: str):
        return [lang_book for lang_book in self.ToDict() if lang in lang_book["Language"]]

    def DownloadBooks(self, TemporaryDirectory: str, lang = None):
        BookList = dict()
        if lang is not None:
            BookList = self.FilerOnLanguage(lang)
        else:
            BookList = self.ToDict()
        
        for BookDownload in BookList:
            if not os.path.exists(os.path.join(TemporaryDirectory, f"{BookDownload['Language'].replace(';', '')}_book_{BookDownload['Text#']}.epub")):
                BookResponse = requests.Session().get(f"https://www.gutenberg.org/ebooks/{BookDownload['Text#']}.epub.images", timeout=5)
                if BookResponse.status_code == 200:
                    with open(os.path.join(TemporaryDirectory, f"{BookDownload['Language'].replace(';', '')}_book_{BookDownload['Text#']}.epub"), "wb") as BookFile:
                        BookFile.write(BookResponse.content)
                        print(f"The book {BookDownload['Title']} has been downloaded")
                else:
                    print(f"Error downloading book {BookDownload['Text#']}: HTTP Error {BookResponse.status_code}")


if __name__ == "__main__":
    config = dotenv_values(".env")
    GuthenbergCollection = RemoteBookCollection(config["GUTHENBERGLINK"]).DownloadBooks(config["TMPDIR"], "de")