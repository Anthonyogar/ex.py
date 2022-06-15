from ast import For
import json
from difflib import get_close_matches


words = json.load(open(r"week2./words.json", "r"))


while True:
    word = input("Enter wors: ").lower()
    if word in words:
        meaning = words.get(word)
        print()
    for index, n in enumerate(meaning, 1):
         print(f"{index}. \t{n}")
         
    else:
        alternatives = get_close_matches(word, words.keys(), 7)
        print(f"(word)words not found!!! Do you mean any of the following")
        print(alternatives)