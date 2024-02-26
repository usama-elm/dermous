import json
import sqlite3
import os

# Connect to SQLite database
conn = sqlite3.connect('words_database.db')

# Create cursor object
c = conn.cursor()

# Drop the table if it exists
c.execute('DROP TABLE IF EXISTS words')

# Create table
c.execute('''
    CREATE TABLE words(
        word TEXT,
        gender TEXT,
        article TEXT,
        word_type TEXT,
        translation TEXT,
        example_sentences TEXT,
        usage_frequency INTEGER,
        ipa_code TEXT,
        verb_auxiliary TEXT,
        difficulty_level TEXT,
        irregular BOOLEAN,
        present_3rd_form_singular TEXT,
        past_perfect TEXT,
        preterite TEXT,
        frequency_scale INTEGER
    )
''')

# Path to directory with JSON files
json_dir = 'word_data'

# For each JSON file
for file_name in os.listdir(json_dir):
    if file_name.endswith('.json'):
        try:
            # Open the JSON file
            with open(os.path.join(json_dir, file_name), 'r') as f:
                # Load JSON data
                data = json.load(f)

                # Extract example sentences as a string
                example_sentences = json.dumps(data.get('example_sentences'))

                # Insert data into table
                c.execute('''
                    INSERT INTO words VALUES (
                        :word,
                        :gender,
                        :article,
                        :word_type,
                        :translation,
                        :example_sentences,
                        :usage_frequency,
                        :ipa_code,
                        :verb_auxiliary,
                        :difficulty_level,
                        :irregular,
                        :present_3rd_form_singular,
                        :past_perfect,
                        :preterite,
                        :frequency_scale
                    )
                ''', {
                    'word': data.get('word'),
                    'gender': data.get('gender'),
                    'article': data.get('article'),
                    'word_type': data.get('word_type'),
                    'translation': data.get('translation'),
                    'example_sentences': example_sentences,
                    'usage_frequency': data.get('usage_frequency'),
                    'ipa_code': data.get('ipa_code'),
                    'verb_auxiliary': data.get('verb_auxiliary'),
                    'difficulty_level': data.get('difficulty_level'),
                    'irregular': data.get('irregular'),
                    'present_3rd_form_singular': data.get('present_3rd_form_singular'),
                    'past_perfect': data.get('past_perfect'),
                    'preterite': data.get('preterite'),
                    'frequency_scale': data.get('frequency_scale')
                })

        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

# Commit changes and close connection
conn.commit()
conn.close()

