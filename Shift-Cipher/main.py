# W4RM15H
# Caeser Cipher
# 22.08.18

from os import system
import time
from termcolor import colored as c

def starting_program():
    system("clear")
    print(c("Caeser Cipher!", 'green'))
    print()
    print(c("Type e/d to select you function", 'green'))
    #Taking user input
    user_input = input(c("Encrypt or decrypt: ", 'green'))
    choice = user_input.lower()

    if choice == "e":
        encrypting_text()
    elif choice == 'd':
        decrypting_text()
    else:
        print("Yeah nah, not a valid entry aye.")
        time.sleep(2)
        starting_program()


def encrypting_text():
    # requesting which word to cipher.
    word = str(input(c("Enter phrase to encrypt: ", 'green')))
    # how many position to shift each letter
    shift = int(input(c("Shift: ", 'green')))
    # added new line to have pretty output
    print()
    # declaring cipher variable to be of type list
    cipher = list()
    # iterating trough each character in word
    for item in word:
        # translanting each characher in word to new character
        # and appending it to cipher list
        cipher.append(chr(ord(item) + shift))
    # printing word
    print(c("Unencrypted Phrase", 'green'))
    print(c(word, 'green'))
    print()
    # printing ciphered word
    print(c("Encrypted Phrase", 'green'))
    print(c(''.join(cipher), 'green'))
    print()
    ctn = input(c("press enter to ctn...", 'green'))
    starting_program()

def decrypting_text():
    # requesting which word to cipher.
    word = str(input(c("Enter Phrase to Decrypt: ", 'green')))
    # how many position to shift each letter
    shift = int(input(c("Shift: ", 'green')))
    # added new line to have pretty output
    print()
    # declaring cipher variable to be of type list
    cipher = list()
    # iterating through each character in word
    for item in word:
        # translanting each characher in word to new character
        # and appending it to cipher list
        cipher.append(chr(ord(item) - shift))
    # printing word
    print(c("Encrypted Phrase", 'green'))
    print(c(word, 'green'))
    print()
    # printing ciphered word
    print(c("Decrypted Phrase", 'green'))
    print(c(''.join(cipher), 'green'))
    print()
    ctn = input(c("press enter to ctn...", 'green'))
    starting_program()

if __name__ == '__main__':
    starting_program()
