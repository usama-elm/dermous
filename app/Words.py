import csv
from fasttext.FastText import _FastText

from dotenv import dotenv_values

class Word():
    def __init__(self, WordContent: str, Lang: str):
        self.WordContent = WordContent
        self.Lang = Lang

    def IsLanguageWord(self):
        TargetLanguage = "__label__" + self.Lang
        config = dotenv_values(".env")
        LoadedModel = _FastText(model_path=config["MODEL"])
        try:
            PredictedLanguage, P = LoadedModel.predict(self.WordContent) # Here P is the probability like in statistics
            if PredictedLanguage[0] == TargetLanguage and P[0] > 0.75:
                return True
        except Exception as e:
            raise e
        return False

    def ReplaceCharacterLang(self):
        return self.WordContent.replace("ue", "ü").replace("ae", "ä").replace("oe", "ö").replace("œ", "ö")
    
    def ToString(self):
        return self.WordContent
    
# if __name__ == "__main__":
#     example = Word(WordContent="geburstag", Lang="de").IsLanguageWord()