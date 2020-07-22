#!============================================== Python Program 12 ============================================!#
#============================================= Rolling Dice And Toss ==========================================



import Prog_14 as p
import time

x=True

while x:
	choice=str(input("\tR -> Roll dice\n\tT -> Toss\n\tE -> Exit \n\t>>> "))
	if choice.capitalize()=="R":
		inp=int(input("Enter number of times : "))
		print("\nNumber of possible outcomes are\n\t",6**inp)
		for y in p.dice(inp).split():
			print("   "+str(y))
			time.sleep(1)
	elif choice.capitalize()=="T":
		inp=int(input("Enter number of times : "))
		print("\nNumber of possible outcomes are\n\t",6**inp)
		for y in p.toss(inp).split():
			print("   "+str(y))
			time.sleep(1)
	elif choice.capitalize()=="E":
		exit()
	else:
		print("Enter A Valid Choice")