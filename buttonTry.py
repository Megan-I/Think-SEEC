#!/user/bin/bash/python

import keyboard
import time
from rpi_ws281x import PixelStrip, Color
import argparse
import question
import openFile
import screens
import scoring

LED_COUNT = 16		#number of LED Pixels
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255	#255 is the  brightest, 0 is the darkest
LED_INVERT = False
LED_CHANNEL = 0


class Button(object):
	color = Color(0,0,0)
	led = 0
	value = 0

	def __init__(self, color, led, value):
		self.color = color
		self.led = led
		self.value = value

def make_button(led, value):
	if(value == 0):
		color = Color(0,0,0)
	if(value == 1):
	 	color = Color(0,255,0)
	if(value == 2):
		color = Color(255,0,0)

	button = Button(color, led, value)
	return button

class Flag(object):
	scoreFlag = False
	startFlag = False
	def __init__(self, flag):
		self.scoreFlag = flag
		self.startFlag = flag
def make_flag():

	f = Flag(False)
	return f

def clear(f):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
		strip.show()

	button0.value = 0
	button1.value = 0
	button2.value = 0
	button3.value = 0
	button4.value = 0
	button5.value = 0
	button6.value = 0
	button7.value = 0

	print "\033c"
	f.startFlag = True


def scoreFlag(Sflag):
	#scores the questions
	num = 4
	Sflag.scoreFlag = True



def printAnimals():
	print("Monkey\t\tDog")

def utdColor():
	for i in range(strip.numPixels()):
		even = i % 2
		if(even == 0):
			#official burnt orange color from ut color guidlines
			strip.setPixelColor(i, Color(191,87,0))
			#but we dont want that because we are utd and we use a slightly different orange
			#here is utds official orange:
			#strip.setPixelColor(i, Color(232,117,0))
			strip.show()
		else:
			#utds official green color: is too blue for the leds
			strip.setPixelColor(i, Color(55,200,10))
			strip.show()

	#time.sleep(100)
def getButtonsPressed():
	scoreNum = 0

	#button 0 holds the 1s place

	if(button0.value == 0):
		scoreNum += 2
	elif(button0.value == 1):
		scoreNum += 1
	elif(button0.value == 2):
		scoreNum += 0

	#button 1 holds the 10s place

	if(button1.value == 0):
		scoreNum += 2 * 10
	elif(button1.value == 1):
		scoreNum += 1 * 10
	elif(button1.value == 2):
		scoreNum += 0  #bc anything times 0 is 0

	#button 2 holds the 100s place

	if(button2.value == 0):
		scoreNum += 2 * 100
	elif(button2.value == 1):
		scoreNum += 1 * 100
	elif(button2.value == 2):
		scoreNum += 0

	#button 3 holds the 1000s place

	if(button3.value == 0):
		scoreNum += 2 * 1000
	elif(button3.value == 1):
		scoreNum += 1 * 1000
	elif(button3.value == 2):
		scoreNum += 0

	#button 4 holds the 10000s place

	if(button4.value == 0):
		scoreNum += 2 * 10000
	elif(button4.value == 1):
		scoreNum += 1 * 10000
	elif(button4.value == 2):
		scoreNum += 0

	#button 5 holds the 100000

	if(button5.value == 0):
		scoreNum += 2 * 100000
	elif(button5.value == 1):
		scoreNum += 1 * 100000
	elif(button5.value == 2):
		scoreNum += 0

	#button 6 holds the 1000000

	if(button6.value == 0):
		scoreNum += 2 * 1000000
	elif(button6.value == 1):
		scoreNum += 1 * 1000000
	elif(button6.value == 2):
		scoreNum += 0

	#button 7 holds the 10000000

	if(button7.value == 0):
		scoreNum += 2 * 10000000
	elif(button7.value == 1):
		scoreNum += 1 * 10000000
	elif(button7.value == 2):
		scoreNum += 0

	#if button 7 is zero it wont show up in the number so
	#add 100000000 just to be safe

	scoreNum += 100000000


	return scoreNum

def changeColor(buttonx):
	buttonx.value += 1

	val = buttonx.value
	if(val == 3):
		buttonx.value = 0
		buttonx.color = Color(0,0,0)
	if(val == 0):
		buttonx.color = Color(0,0,0)
	if(val == 1):
		buttonx.color = Color(0,255,0)
	if(val == 2):
		buttonx.color = Color(255,0,0)

	strip.setPixelColor(buttonx.led, buttonx.color)
	strip.show()

if __name__ == '__main__':
	#parser = argparse.ArgumentParser()
	#parser.add_argument('-c', '--clear', action='store true', help='clear the display on exit')
	#args = parser.parse_args()


	strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

	strip.begin()
	num = 4


	button0 = make_button(0,0)
	button1 = make_button(1,0)
	button2 = make_button(2,0)
	button3 = make_button(3,0)
	button4 = make_button(4,0)
	button5 = make_button(5,0)
	button6 = make_button(6,0)
	button7 = make_button(7,0)

	f = make_flag()


	keyboard.add_hotkey('0',lambda: changeColor(button0))
	keyboard.add_hotkey('1',lambda:	changeColor(button1))
	keyboard.add_hotkey('2',lambda: changeColor(button2))
	keyboard.add_hotkey('3',lambda: changeColor(button3))
	keyboard.add_hotkey('4',lambda: changeColor(button4))
	keyboard.add_hotkey('5',lambda: changeColor(button5))
	keyboard.add_hotkey('6',lambda: changeColor(button6))
	keyboard.add_hotkey('7',lambda: changeColor(button7))
	keyboard.add_hotkey('9',lambda: clear(f))
	keyboard.add_hotkey('8',lambda: scoreFlag(f))



	screens.intro()

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)



#	f.startFlag = True
#	q1 = question.make_Q_Object(qu, True, False, False, True, False, False, True, True)


	file = openFile.openFile()

	q1 = openFile.readFile(file, 0)
	q2 = openFile.readFile(file, 1)
	q3 = openFile.readFile(file, 2)
	q4 = openFile.readFile(file, 3)
	q5 = openFile.readFile(file, 4)
	q6 = openFile.readFile(file, 5)
	q7 = openFile.readFile(file, 6)
	q8 = openFile.readFile(file, 7)
	q9 = openFile.readFile(file, 8)
	q10 = openFile.readFile(file, 9)
	openFile.closeFile(file)

	screens.questionScreen(q1.question)

	score1 = -3

	while(q1.answered == False):
		if(f.scoreFlag == True):
			q1.answered = True
			user = getButtonsPressed()
			key = q1.key
			score1 = scoring.score(user,key)
			if(score1 == -1):
				screens.incomplete()
				screens.questionScreen(q1.question)
				q1.answered = False
				f.scoreFlag = False


	f.scoreFlag = False
	clear(f)

	f.startFlag = False
	screens.littleScore(score1)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	clear(f)
#	f.startFlag = True

	screens.questionScreen(q2.question)



	while(q2.answered == False):
		if(f.scoreFlag == True):
			q2.answered = True
			user2 = getButtonsPressed()
			key2 = q2.key
			score2 = scoring.score(user2, key2)
			if(score2 == -1):
				screens.incomplete()
				screens.questionScreen(q2.question)
				q2.answered = False
				f.scoreFlag = False


	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score2)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q3.question)


	while(q3.answered == False):
		if(f.scoreFlag == True):
			q3.answered = True
			user3 = getButtonsPressed()
			key3 = q3.key
			score3 = scoring.score(user3, key3)
			if(score3 == -1):
				screens.incomplete()
				screens.questionScreen(q3.question)
				q3.answered = False
				f.scoreFlag = False

	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score3)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q4.question)


	while(q4.answered == False):
		if(f.scoreFlag == True):
			q4.answered = True
			user4 = getButtonsPressed()
			key4 = q4.key
			score4 = scoring.score(user4, key4)
			if(score4 == -1):
				screens.incomplete()
				screens.questionScreen(q4.question)
				q4.answered = False
				f.scoreFlag = False



	f.scoreFlag = False
 	clear(f)
	f.startFlag = False

	screens.littleScore(score4)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)


	screens.questionScreen(q5.question)


	while(q5.answered == False):
		if(f.scoreFlag == True):
			q5.answered = True
			user5 = getButtonsPressed()
			key5 = q5.key
			score5 = scoring.score(user5, key5)
			if(score5 == -1):
				screens.incomplete()
				screens.questionScreen(q5.question)
				q5.answered = False
				f.scoreFlag = False

	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score5)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q6.question)


	while(q6.answered == False):
		if(f.scoreFlag == True):
			q6.answered = True
			user6 = getButtonsPressed()
			key6 = q6.key
			score6 = scoring.score(user6, key6)
			if(score6 == -1):
				screens.incomplete()
				screens.questionScreen(q6.question)
				q6.answered = False
				f.scoreFlag = False


	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score6)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q7.question)


	while(q7.answered == False):
		if(f.scoreFlag == True):
			q7.answered = True
			user7 = getButtonsPressed()
			key7 = q7.key
			score7 = scoring.score(user7, key7)
			if(score7 == -1):
				screens.incomplete()
				screens.questionScreen(q7.question)
				q7.answered = False
				f.scoreFlag = False


	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score7)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q8.question)

	while(q8.answered == False):
		if(f.scoreFlag == True):
			q8.answered = True
			user8 = getButtonsPressed()
			key8 = q8.key
			score8 = scoring.score(user8,key8)
			if(score8 == -1):
				screens.incomplete()
				screens.questionScreen(q8.question)
				q8.answered = False
				f.scoreFlag = False


	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score8)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q9.question)

	while(q9.answered == False):
		if(f.scoreFlag == True):
			q9.answered = True
			user9 = getButtonsPressed()
			key9 = q9.key
			score9 = scoring.score(user9, key9)
			if(score9 == -1):
				screens.incomplete()
				screens.questionScreen(q9.question)
				q9.answered = False
				f.scoreFlag = False


	f.scoreFlag = False
	clear(f)
	f.startFlag = False

	screens.littleScore(score9)

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	screens.questionScreen(q10.question)

	while(q10.answered == False):
		if(f.scoreFlag == True):
			q10.answered = True
			user10 = getButtonsPressed()
			key10 = q10.key
			score10 = scoring.score(user10,key10)
			if(score10 == -1):
				screens.incomplete()
				screens.questionScreen(q10.question)
				q10.answered = False
				f.scoreFlag = False


	clear(f)
	f.startFlag = False


	screens.littleScore(score10)

	screens.outro()

	while(f.startFlag == False):
		utdColor()
		time.sleep(1)

	finalScore = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10


	screens.bigScore(finalScore)
