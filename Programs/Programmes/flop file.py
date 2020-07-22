#!============================================== Python Program 12 ============================================!#
#=============================================== Database in Python ============================================#


db=open("school.txt",'r')
# db.write("Name \t Class \t Roll Number \t Section\n\n")

running=True
while running:
    choice=str(input(" A -> Append a record to Database \n L -> Least Common Multiple \n E -> Exit \n\t>>>"))
    if choice.capitalize()=="A":
        snum=int(input("Enter Serial Number : "))
        name=str(input("Enter Name : "))
        clas=str(input("Enter Class : "))
        section=str(input("Enter Section : "))
        db=open("school.txt",'a')
        db.write(str(snum)+"\t|\t"+name+"\t|\t"+clas+"\t|\t"+section)
        db=open("school.txt",'r')

	# elif choice.capitalize()=="L":
	# 	num1=int(input("Enter First Number : "))
	# 	num2=int(input("Enter Second Number : "))
	# 	print("Least common multiple of the numbers is : ",p.lcm(num1,num2))
    elif choice.capitalize()=="E":
        running=False
    else:
        print("\nEnter A Valid Choice")


print(db.readlines())