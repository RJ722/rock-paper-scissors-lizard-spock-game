# Rock - Paper - Scissors - Lizard - Spock Game

import random

nameList = ["Rock", "Spock", "Paper", "Lizard", "Scissors"]

def indexMaker(li, ch):
	'''
	This returns the index of the particular item in a list.
	'''
	for i in range(len(li)):
		if li[i] == ch:
			return i
		else:
			pass

def nameToNumber(name):
	'''
	This function converts the given choice t its corresponding number using:
	Rock -- 0
	Spock -- 1
	Paper -- 2
	Lizard -- 3
	Scissors -- 4
	'''
	if indexMaker(nameList, name) != None:
		number = indexMaker(nameList, name)
		return number
	else:
		print("No such option!!\nGame Aborted!")

def NumberToName(number):
	'''
	This function converts the given number from 0 to 4 to the corresponding item using:
	0 -- Rock
	1 -- Spock
	2 -- Paper
	3 -- Lizard
	4 -- Scissors
	'''
	try:	
		name = nameList[number]
		return name
	except:
		print("Please enter a valid option!!")

while True:
	# Ask for name:
	usrName = input("Please enter your name: ")

	# Greetings and tell about the rules
	print(" \t \tComputer welcomes %s to the world of ROCK-PAPER-SCISSORS-LIZARD-SPOCK" % (usrName))
	print("\t\t" + "-" * 67 + "-" * len(usrName))
	print(" It's very simple\n","-" * 16,"\n Scissors cuts paper\n Paper covers rock\n Rock crushes lizard\n Lizard poisons Spock\n Spock smashes scissors\n Scissors decapitates lizard\n Lizard eats paper\n Paper disproves Spock\n Spock vaporizes rock\n\n And as it always has been\n Rock crushes scissors\n")
	print(" CAUTION: CASE - SENSITIVE")
	print(" " + "-" * 7 + "\n")

	# Ask for choice
	usrInput = input(" \t \t \t Your choices are: \tRock, Paper, Scissors, Lizard, Spock \n\n Please enter your choice: ")

	# Generates Computers result:
	compInputNum = random.randrange(5)


	def game(usrInput):
		'''
		It decides winner on the basis that the user can only win if computer's choice is such that it is 3 more or 4 more than user's choice in cyclic manner, user draws with computer if they have same choice and computer wins in all other cases.
		'''
		try:
			usrInputNum = nameToNumber(usrInput)
			draw = "No one"
			# Decide the winner!
			if compInputNum == ((usrInputNum + 3) % 5) or compInputNum == ((usrInputNum + 4) % 5):
				winner = usrName
			elif compInputNum == usrInputNum:
				winner = draw
			else:
				winner = "Computer"
			
			# Evaluate compInput in string for to get it printed
			compInput = NumberToName(compInputNum)
			
			# Print the results!
			screenWidth = 113
			print("-" * screenWidth)
			print("\t \t \t \t \t %s's choice is %s \n \t \t \t \t \t Computer's choice is %s " % (usrName, usrInput, compInput))
			print(" \n \t \t \t \t \t %s wins!!" % (winner))
			if winner == draw:
				print("\t \t \t \t \t Oooo! That was a close one!!")
			
			print("-" * screenWidth)
			return winner
		except:
			pass

	if __name__ == "__main__":
		game(usrInput)