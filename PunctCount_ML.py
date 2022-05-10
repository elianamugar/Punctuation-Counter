#requires download of NLTK in Python
import os
import nltk
from nltk.corpus import *
import string

def main():
    # modify path for where files are on machine
    path = "/Users/EMWork/Desktop/Boston University/EVL/Map Lemon Analysis/Data/Assigned Sex Data"
    for text_file in os.listdir(path):
        if '.txt' in text_file:
            print("We are in " + text_file)
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            my_file = os.path.join(THIS_FOLDER, text_file)
            f = open(my_file, 'r+')
            raw = f.read()

            # tags all words with corresponding part-of-speech in user's text file choice
            update_corpus = ""

            count_commas = 0
            count_semicolons = 0
            count_periods = 0
            count_parentheses = 0
            count_dashes = 0
            count_colons = 0

            for i in range(len(raw)):
                if raw[i] == ",":
                    count_commas += 1
                elif raw[i] == ";":
                    count_semicolons += 1
                elif raw[i] == ".":
                    count_periods += 1
                elif raw[i] in "()":
                    count_parentheses += 1
                elif raw[i] == "-":
                    count_dashes +=1
                elif raw[i] == ":":
                    count_colons += 1

            update_corpus += "Commas: " + str(count_commas) + "\n" + \
                "Semicolons: " + str(count_semicolons) + "\n" + \
                    "Periods: " + str(count_periods) + "\n" + \
                        "Parentheses: " + str(count_parentheses) + "\n" + \
                            "Dashes: " + str(count_dashes) + "\n" + \
                                "Colons: " + str(count_colons)

            f = open(str(input("Enter filename for which you want the data text to be exported (with .txt): \n")), "w")
            f.write(update_corpus)

while True:
    answer = input("Run the 'Punctuation Counter' program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break
