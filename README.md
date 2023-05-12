# DerMous
The objective is to create an open source version of Duden-API. Necessary for future german-learning app projects.

## How it was done
As of now, the basic info comes from The Gutenberg Porject German books. In the future the source will be expanded to DW, German Wikipedia/Wikitionary and other online public-broadcasting services. With the advances of Wisper.cpp I will also download videos in German from youtube and transcribe them so that I can get a good, full corpus of German words.

This project is both a compilation of scripts (still being worked on) and JSON end files which will turn into a good data-pipeline from source to extracted CSV (golden csv) which for now requests OpenAI GPT-3.5-turbo for the JSON files but in the future an open source LLM will be used.
Added to that there will be a future local API so that one can request the words in a self-contained way. Once the project matures a full Docker image will be furnished so the end user goes through the least hurdles.

## Requirements
- Python3.10+
- pip
- [Language Identification Bin](https://fasttext.cc/docs/en/language-identification.html) to be put in src/ folder
- csv, fasttext, ebooklib, nltk, pandas, requests, regex, openai
- An OpenAI api key

For now there are ~2k words trated that give this format ```json
{
    "word": "wirksamkeit",
    "gender": "f",
    "article": "die",
    "word_type": "noun",
    "translation": "effectiveness",
    "example_sentences": [
        {
            "de": "Die Wirksamkeit des Medikaments wurde in klinischen Studien getestet.",
            "en": "The effectiveness of the medication was tested in clinical trials."
        },
        {
            "de": "Die Wirksamkeit der Maßnahmen zur Eindämmung des Virus ist umstritten.",
            "en": "The effectiveness of the measures to contain the virus is controversial."
        }
    ],
    "usage_frequency": 7,
    "ipa": "/ˈvɪʁkzamlɪçkaɪt/",
    "verb_auxiliary": null,
    "difficulty_level": "B1",
    "irregularities": null,
    "present_3s": null,
    "past_perfect": null,
    "preterite": null,
    "frequency_scale": 7
}
```
## To-Do List
- Refactor code so it is an OOP-cohesive project
- Test Vicuna-7B, MPT and Google's Bard to have better JSON results.
- Parallelize the tratment so that more words can be asked to the API and received
- Create a cost and word tracker for the OpenAI GPT-3.5-turbo model
- Add other text sources (Wikipedia, other open Source books, MIT Licence compatible web-based scrapping, C4)
- Create a Video-to-text tool based on Whisper.cpp and a German model to add more corpus
- Create a FastAPI based API
- Create a elf-contained Docker image

