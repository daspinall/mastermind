#Makes mastermind, a game where you play against the computer
#  to guess a series of colors in a set number of moves, while
#  getting feedback from the computer.

from random import randint

def mastermind():

	guesses = 0
	difficulty = raw_input("Difficulty? Easy, intermediate, or hard?")
	
	while True:
		if lower(difficulty) == "easy":
			guesses = 20
			break
		elif lower(difficulty) == "intermediate":
			guesses = 15
			break
		elif lower(difficulty) == "hard":
			guesses = 10
			break
		else:
			difficulty = raw_input("Enter again? Easy, intermediate, or Hard?")

	#red, green, blue, yellow, orange, or purple
	possible_colors = [r, g, b, y, o, p]

	master_code = []

	for color in range(5):
		master_code[color] = possible_colors[randint(0, 5)]