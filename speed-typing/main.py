#w4rm15h
#50 Projects
#43. Typing Practice for Accuracy and Speed
import os
import time
from data import *
import random
#FIGURE OUT HOW TO FORMAT THE TIME
def time_convert(sec):
	mins = sec // 60
	sec = sec % 60
	hours = mins // 60
	mins = mins % 60
	speed = ("{0}:{1}:{2}".format(int(hours),int(mins),sec))
	print(speed)
	return(speed)

def sentenceTest():
	os.system("clear")
	print("Your Sentence\n")
	sentence = random.choice(quotes)
	print(sentence)
	print()
	
	yep = input("Press ENTER to begin.")
	startTime = time.time()	
	typeTest = input("")
	endTime = time.time()	
	timeLapsed = endTime - startTime
	print(f"****{timeLapsed}****")
	speed = time_convert(timeLapsed)
	os.system('clear')
	print("The results are in...")
	print()
	print(f"THE PHRASE: {sentence}")
	print(f"YOUR GO   : {typeTest}")
	print(speed)
	test = input()
	
#LET US BEGIN
def mainMenu():
	os.system("clear")
	print("Welcome to the typing test.")
	print()
	print("\n1. Sentence Challenge.\n   complete the sentence as fast as possible.\n   Hitting enter completes the round.")
	print()
	print("2. Paragraph Challange.")
	print()
	choice = input("[1,2]: ")

	if choice == "1":
		sentenceTest()


mainMenu()

	
	