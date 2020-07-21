#!/user/bin/bash/python

#this will hold the screen functions

def intro():
	print("\033c")
	print("\n\n\tWelcome to Think!")
	print("\n\n\tHow to play: ")
	print("\n\t -Questions will show up on this screen.")
	print("\n\t -The question will be either true or false\n\t  for the animals listed.")
	print("\n\t -You have to THINK and figure out wich \n\t  are true and wich animals are false.")
	print("\n\t -To make your choice press the buttons \n\t  once for true and twice for false.")
	print("\n\t -The button will glow green if true is selected \n\t  and red if false is selected.")
	print("\n\t -If the button is not lit then no choice has been selected.")
	print("\n\t -Please select a choice for each animal before \n\t  you move onto the next question.")
	print("\n\n\tHave fun and dont forget to THINK!")

	print("\n\nPress button 9 to begin.")

def littleScore(score):

	if(score >= 7):
		print("\n\n\tGood Job!")
	elif(score == 5 or  score == 6):
		print("\n\n\tSo close! You're almost there!")
	else:
		print("\n\n\tBetter luck next time")

	print "\n\t\tScore: " ,score, "/8\n\t\tTime: ?s"
	print("\nPress 9 to continue to next question")


def bigScore():
	print("\n\t\ttotal score")
	print("\n\t\ttotal time")
	print("\n\n\t\tPlay again?")

def questionScreen(question):
#	print("\033c")
	print(question)
	print("\n1.Dog\t\t2.Kangaroo\n3.Snake\t\t4.Penguin\n5.Turtle\t6.Crow\n7.Goldfish\t8.Horse")


def scoreboard(score):
	print("scoreboard")

def outro():
	print("Final screen test")
	print("\n\n\tYou completed THINK!")
	print("\n\tPress 9 to see your final score!")


def incomplete():
	print("\n\nYou cannot submit the question until ALL buttons have been pressed")
	print("Any button not lit up has not been pressed")
	print("\n\n\t Please try again") 
