#w4rm15h
#24/5/21
#Simple Calculator
#Imports
import os
import sys
import time

keys = ['-', '+', '*', '/']
method = ""


def user_input():
    while True:
        os.system("clear")
        print("w4rm15h Calculator")
        eq = input(": ").lower()
        e = list(eq)
        for i in e:
            if i in keys:
                met = int(i)
                method = keys["{0}".format(met)]
                print("Method = {0}".format(method))
                postition = eq.index[method]
                print("The position of the key is {0}".format(postition))

        ctn = input('Enter to continue...')

if __name__ == "__main__":
    user_input()