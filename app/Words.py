import csv
import fasttext
from config import ModelDirectory

LoadedModel = fasttext.load_model(ModelDirectory)

class Word():
    def __init__(self, WordContent: str, Lang: str):
        self.WordContent = WordContent
        self.Lang = Lang

    def IsLanguageWord(self):
        TargetLanguage = "__label__" + self.Lang
        try:
            PredictedLanguage, P = LoadedModel.predict(self.WordContent) # Here P is the probability like in statistics
            if PredictedLanguage[0] == TargetLanguage and P[0] > 0.9:
                return True
        except Exception as e:
            raise e
        return False

    def ReplaceCharacterLang(self):
        return self.WordContent.replace("ue", "ü").replace("ae", "ä").replace("oe", "ö").replace("œ", "ö")