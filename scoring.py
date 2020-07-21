#!/user/bin/bash/python


#needed for integer division = //

from __future__ import division

#this will be the scoring section

#bit array?

	#each button gets a bit
	#how to figure out percentage correct
	#10101010 is the key
	#10001000 is what is pressed by the user
	#somehow get program to see that two places are wrong
	#easy peasy


	#I might not do it this way^^^


	#gonna try to do t this way
	#passed a number with 0s 1s and 2s
	#0s mean true
	#1s mean false
	#2s mean not answered
	#any number with 2s gets sent back and warning screen apears
	#if not check number against key number
	#any difference results in point lost
	#total points is 10
	#number from 0-10 is returned and is the score


	#Passed: input scoere and score key
	#returned 0-10 score

def score(user, key):
	numScore = 0
	#incomplete = False

	for x in range(0,8):
		place =	user % 10

		if(place == 2):
			numScore = -1 #incomplete
			break
		else:
			keyPlace = key % 10
			if(keyPlace == place):
				numScore += 1

		user = user // 10
		key = key // 10


	return numScore
