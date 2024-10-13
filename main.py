import sys
import re
import numpy as np

def main():
    #czytam input i dziele na linie
    input_data = sys.stdin.read().strip().split('\n')
    #czytam ile dokumentow i jakich
    num_documents = int(input_data[0])
    documents = input_data[1:num_documents + 1]
    #czytam ile slow i jakich
    num_words = int(input_data[num_documents + 1])
    words_to_find = input_data[num_documents + 2:num_documents + 2 + num_words]

    #slownik na wynikii
    results = {}

    #petla ktora iteuje po slowach do znalezienia
    for word in words_to_find:
        word_counts = []
        for index, document in enumerate(documents):
            processed_doc = re.sub(r'[^\w\s]', ' ', document.lower())
            words = processed_doc.split()
            count = words.count(word)
            if count > 0:  # Sprawdzenie czy słowo występuje w dokumencie
                word_counts.append((index, count))
        #sortowanie
        indexes_together = [idx for idx, _ in sorted(word_counts, key=lambda x: x[1], reverse=True)]
        results[word] = indexes_together

    #wypisanie wyniku
    for word, indexes_together in results.items():
        print(f"'{word}': {indexes_together}")

if __name__ == "__main__":
    main()
