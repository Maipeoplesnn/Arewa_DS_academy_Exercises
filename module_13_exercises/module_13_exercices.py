## 💻 File Handling Exercises:

### Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
def obama():
   from pathlib import Path
   path = Path(r'C:\Users\hp\Desktop\Arewa_DS_Training\30-Days-of-Python\data\obama_speech.txt')
   contentlines = path.read_text().splitlines()
   contentwords = path.read_text().split()
   print(f"the total number of lines in the file is {len(contentlines)}")
   print(f"the total number of words in the file is {len(contentwords)}")

   # b) Read michelle_obama_speech.txt file and count number of lines and words
def michelle():
    from pathlib import Path
    path = Path(r'C:\Users\hp\Desktop\Arewa_DS_Training\30-Days-of-Python\data\michelle_obama_speech.txt')
    contentlines = path.read_text().splitlines()
    contentwords = path.read_text().split()
    print(f"the total number of lines in the file is {len(contentlines)}")
    print(f"the total number of words in the file is {len(contentwords)}")

   # c) Read donald_speech.txt file and count number of lines and words
def donald():
    from pathlib import Path
    path = Path(r'C:\Users\hp\Desktop\Arewa_DS_Training\30-Days-of-Python\data\donald_speech.txt')
    contentlines = path.read_text().splitlines()
    contentwords = path.read_text().split()
    print(f"the total number of lines in the file is {len(contentlines)}")
    print(f"the total number of words in the file is {len(contentwords)}")

   # d) Read melina_trump_speech.txt file and count number of lines and words
def melina():
    from pathlib import Path
    path = Path(r'C:\Users\hp\Desktop\Arewa_DS_Training\30-Days-of-Python\data\melina_trump_speech.txt')
    contentlines = path.read_text().splitlines()
    contentwords = path.read_text().split()
    print(f"the total number of lines in the file is {len(contentlines)}")
    print(f"the total number of words in the file is {len(contentwords)}")

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def most_spoken_languages(file, n):
    with open(file, 'r') as f:
        data = json.load(f)

    languages = {}
    for country in data:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    most_spoken = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:n]
    return most_spoken

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

import json

def most_populated_countries(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)

    countries = []
    for country in data:
        countries.append({'country': country['name'], 'population': country['population']})

    most_populated = sorted(countries, key=lambda x: x['population'], reverse=True)[:n]
    return most_populated


### Exercises: Level 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
def extract_emails(file):
    with open(file, 'r') as data:
        contents = data.read()
        emails = re.findall()

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words,
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. 
# Your function will return an array of tuples in descending order. Check the output

import re
from collections import Counter

def find_most_common_words(file_or_string, n):
    if isinstance(file_or_string, str) and file_or_string.endswith('.txt'):
        with open(file_or_string, 'r') as f:
            text = f.read()
    else:
        text = file_or_string

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(n)
    return most_common_words



'''6. Use the function, find_most_frequent_words to find:
   a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)'''
# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and 
   # it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory
import numpy as np
from scipy import spatial
import nltk
import word_tokenize
import stopwords
import WordNetLemmatizer

def calculate_similarity(text1, text2):
    # Tokenize the texts
    tokens1 = word_tokenize(text1)
    tokens2 = word_tokenize(text2)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens1 = [word for word in tokens1 if word.lower() not in stop_words]
    tokens2 = [word for word in tokens2 if word.lower() not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens1 = [lemmatizer.lemmatize(word) for word in tokens1]
    tokens2 = [lemmatizer.lemmatize(word) for word in tokens2]

    # Create a set of all unique tokens
    all_tokens = set(tokens1 + tokens2)

    # Create a dictionary to store the frequency of each token
    freq_dict1 = {}
    freq_dict2 = {}

    # Calculate the frequency of each token in the first text
    for token in all_tokens:
        freq_dict1[token] = tokens1.count(token)

    # Calculate the frequency of each token in the second text
    for token in all_tokens:
        freq_dict2[token] = tokens2.count(token)

    # Create vectors from the frequency dictionaries
    vector1 = list(freq_dict1.values())
    vector2 = list(freq_dict2.values())

    # Calculate the cosine similarity between the two vectors
    similarity = 1 - spatial.distance.cosine(vector1, vector2)

    return similarity

def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

def main():
    # Read the transcripts of Michelle's speeches
    michelle_obama_speech = read_file('michelle_obama_speech.txt')
    melina_trump_speech = read_file('melina_trump_speech.txt')

    # Calculate the similarity between the two speeches
    similarity = calculate_similarity(michelle_obama_speech, melina_trump_speech)

    print("The similarity between Michelle's and Melina's speeches is: ", similarity)

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
import re
from collections import Counter

def find_most_repeated_words(filename, n):
    with open(filename, 'r') as f:
        text = f.read()

    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Find the n most common words
    most_common_words = word_counts.most_common(n)

    return most_common_words

filename = r'C:\Users\hp\Desktop\Arewa_DS_Training\30-Days-of-Python\data\romeo_and_juliet.txt'
n = 10

most_repeated_words = find_most_repeated_words(filename, n)

print("The 10 most repeated words in the romeo_and_juliet.txt are:")
for word, count in most_repeated_words:
    print(f"{word}: {count}")

''' 9. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
   a) Count the number of lines containing python or Python
   b) Count the number lines containing JavaScript, javascript or Javascript
   c) Count the number lines containing Java and not JavaScript.'''

import pandas as pd

def count_lines(filename, words):
    df = pd.read_csv(filename)
    count = 0
    for index, row in df.iterrows():
        for column in row:
            if isinstance(column, str):
                for word in words:
                    if word.lower() in column.lower():
                        count += 1
                        break
    return count

def count_lines_with_not(filename, word1, word2):
    df = pd.read_csv(filename)
    count = 0
    for index, row in df.iterrows():
        found_word1 = False
        found_word2 = False
        for column in row:
            if isinstance(column, str):
                if word1.lower() in column.lower():
                    found_word1 = True
                if word2.lower() in column.lower():
                    found_word2 = True
        if found_word1 and not found_word2:
            count += 1
    return count

filename = r'C:\Users\hp\Desktop\Arewa_DS_Training\30-Days-of-Python\data\hacker_news.csv'


python_count = count_lines(filename, ['python', 'Python'])
print(f"Number of lines containing python or Python: {python_count}")


javascript_count = count_lines(filename, ['JavaScript', 'javascript', 'Javascript'])
print(f"Number of lines containing JavaScript, javascript or Javascript: {javascript_count}")


java_count = count_lines_with_not(filename, 'Java', 'JavaScript')
print(f"Number of lines containing Java and not JavaScript: {java_count}")