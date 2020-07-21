#!/user/bin/bash/python

class Question:
	question = " "
	answered = False
	key = -3

	def isAnswered(boop):
		return answered

	def setAnswered(boo2):
		answered = boo2

	def __init__(self,qu,num):
		self.question = qu

#		print(self.question)
		self.key = int(num)


def make_Q_Object(qstring,num):
	q = Question(qstring,num)
	return q
