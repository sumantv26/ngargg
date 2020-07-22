#!============================================== Python Program 17 ======================================================!#
#================================================== GCD And LCM  =========================================================#

import Prog_16 as p

running=True
while running:
	choice=str(input(" G -> Greatest Common Divisor \n L -> Least Common Multiple \n E -> Exit \n\t>>>"))
	if choice.capitalize()=="G":
		num1=int(input("Enter First Number : "))
		num2=int(input("Enter Second Number : "))
		print("Greatest Number That Divides both numbers is : ",p.gcd(num1,num2))
	elif choice.capitalize()=="L":
		num1=int(input("Enter First Number : "))
		num2=int(input("Enter Second Number : "))
		print("Least common multiple of the numbers is : ",p.lcm(num1,num2))
	elif choice.capitalize()=="E":
		running=False
	else:
		print("\nEnter A Valid Choice")
