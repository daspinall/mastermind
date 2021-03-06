#Makes mastermind, a game where you play against the computer
#  to guess a series of colors in a set number of moves, while
#  getting feedback from the computer.

from random import randint

def mastermind():

	#Initialize a limit and how many guesses are made
	guess_limit = 0
	guesses_made = 0
	difficulty = raw_input("Difficulty? Easy, intermediate, or hard?")
	
	#Establish how difficult the user wants the game
	while True:
		if difficulty.lower() == "easy":
			guess_limit = 20
			break
		elif difficulty.lower() == "intermediate":
			guess_limit = 15
			break
		elif difficulty.lower() == "hard":
			guess_limit = 10
			break
		else:
			difficulty = raw_input("Enter again? Easy, intermediate, or Hard?")

	#Red, green, blue, yellow, orange, or purple
	possible_colors = ["r", "g", "b", "y", "o", "p"]

	#Create the random master code
	master_code = []
	for color in range(0, 5):
		master_code.insert(color, possible_colors[randint(0, 5)])

	print master_code 

	#While the user still has guesses left, let them guess!
	while guesses_made < guess_limit:
		guess = raw_input("Make your guess of five colors! ")

		guess_list = [c for c in guess]

		output = ""

		#Keeps track of where in the list we are and how many exact colors are guessed
		index = 0
		exact_colors = 0
		for color in guess_list:

			output += "Position " + str(index + 1) + ": "

			#Three outputs possible per color: in the exact place, 
			if guess_list[index] == master_code[index]:
				output += "Exact!" + "\n"
				exact_colors += 1
			elif color in master_code:
				output += "Somewhere else!" + "\n"
			else:
				output += "Nope!" + "\n"

			index += 1

		#Print the output if the exact code is guessed
		if exact_colors == 5:
			output = "Congratulations! You beat the mastermind!"
			print output
			break

		#If they didn't get it right, show them the hints
		print output

mastermind()

