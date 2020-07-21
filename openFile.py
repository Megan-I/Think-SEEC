#!/user/bin/bash/pyhton

import question

def openFile():
	file = open("questionsText.txt", "r")
	return file


def readFile(file, line):

	#if(line == 0):
	#	num = file.readline()

#	numOfQuestions = line * 9



#	for x in range(0 , numOfQuestions):
#		empty = file.readline()

	q  = file.readline()
	key = file.readline()



	q1 = question.make_Q_Object(q, key)


	return q1


def closeFile(file):

	file.close()
