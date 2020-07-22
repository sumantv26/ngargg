#!============================================== Python Program 11 ============================================!#
#========================================= Rolling Dice And Toss Module ========================================

import random

def dice(num):
	strr=""
	for x in range(num):
		strr+=str(random.randint(1,6))+" "
	return strr

def toss(num):
	strr=""
	ltoss=["Heads","Tails"]
	for x in range(num):
		strr+=str(ltoss[random.randint(0,1)])+" "
	return strr