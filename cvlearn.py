import fileinput
import csv
from pythainlp.tokenize import word_tokenize

thai_words = set()

for line in fileinput.input("data/prathom-thai.txt"):
    thai_words.add(line.strip())

print(thai_words)

csv_file = csv.reader(fileinput.input("data/validated.tsv"), delimiter='\t')
for row in csv_file:
    if set(word_tokenize(row[2])).issubset(thai_words):
        print(row[1])
        print(row[2])