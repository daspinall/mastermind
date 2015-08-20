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
		if lower(difficulty) == "easy":
			guess_limit = 20
			break
		elif lower(difficulty) == "intermediate":
			guess_limit = 15
			break
		elif lower(difficulty) == "hard":
			guess_limit = 10
			break
		else:
			difficulty = raw_input("Enter again? Easy, intermediate, or Hard?")

	#Red, green, blue, yellow, orange, or purple
	possible_colors = [r, g, b, y, o, p]

	#Create the random master code
	master_code = []
	for color in range(5):
		master_code[color] = possible_colors[randint(0, 5)]

	#While the user still has guesses left, let them guess!
	while guesses_made < guess_limit:
		guess = raw_input("Make your guess! ")

		guess_list = [c for c in guess]

		output = ""

		index = 0
		for color in guess_list:

			output += "Position " + str(index + 1) + ": "

			if guess_list[index] == master_code[index]:
				output += "Exact!"
			elif color is in master_code:
				output += "Somewhere else!" + "\n"


