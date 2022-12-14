Simpl#W4RM15H
#29/08/18
#Word Generater

import random
import os

words = (open('words.txt').readlines())

def words_intro():
    print("Random word generater")
    print("Selecting randoms words for a list.")
    print()
    continue_words = input("Press enter to continue")
    printing_words()

def printing_words():
    print()
    print("Random words")
    print()
    result = ""
    for i in range(0, 4):
        result += random.choice(words) + ""
    print(result)
    print()
    continue_words = input("Press enter to continue")
    printing_words()

if __name__ == "__main__":
    words_intro()