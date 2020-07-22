#!============================================== Python Program 5 ============================================!#
#============================================ Graph with Matplotlib ==========================================#

from matplotlib import pyplot as mp
x=True

while x:
	choice=str(input("\tM -> Make A Custom Graph \n\tR -> Plot Random Graph \n\tE -> Exit \n\t>>> "))
	if choice.capitalize()=="M":
		x,y=[],[]
		num=1
		while num <=1 :
			num=int(input("Enter number of values to input (Greater than 2) : "))
		for i in range(num):
			x.append(int(input("Enter number "+str(i+1)+" x coordinate : ")))
			y.append(int(input("Enter number "+str(i+1)+" y coordinate : ")))
		mp.plot(x,y,color="dodgerblue", linewidth="2.5")
		mp.show()
	elif choice.capitalize()=="R":
			import random
			x,y=[],[]
			for i in range(5):
				x.append(random.randint(0,50))
				y.append(random.randint(0,50))
			mp.plot(x,y,color="coral")
			mp.show()
	elif choice.capitalize()=="E":
		x=False
	else:
		print("Enter A Valid Choice")
