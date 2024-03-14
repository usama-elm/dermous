from Books import *
import os 
import nltk

nltk.download('punkt', download_dir="app/lang")
nltk.download('stopwords', download_dir="app/lang")
nltk.data.path.append("app/lang")

BookCollection(bookCollectionPath="/home/asmy/prj/dermous/.tmp", lang="german", shLang="de").CollectionWordsExport(outputPath=f"{os.path.dirname(__file__)}")
