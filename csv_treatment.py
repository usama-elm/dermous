import csv
import fasttext

def is_german_word(model, word):
    try:
        lang, prob = model.predict(word)
        if lang[0] == '__label__de' and prob[0] > 0.9:
            return True
    except Exception as e:
        pass
    return False

def filter_german_words(input_file, output_file):
    model = fasttext.load_model('lid.176.bin')

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            word = row[0]
            if is_german_word(model, word):
                writer.writerow(row)

        print(f"Filtered German words written to {output_file}")

def replace_characters(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        with open("modified_" + filename, "w", encoding="utf-8", newline='') as modified_file:
            writer = csv.writer(modified_file)
            for row in reader:
                modified_row = [word.replace("ue", "ü").replace("ae", "ä").replace("oe", "ö").replace("œ", "ö") for word
                                in row]
                writer.writerow(modified_row)

filter_german_words('unique_words.csv', 'german_unique_words.csv')
replace_characters("german_unique_words.csv")
