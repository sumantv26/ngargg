#!============================================== Python Program 4 ============================================!#
#============================================ Simple File Operations ==========================================#

x=True

while x:
    choice=str(input("\tC -> Create File \n\tD -> Delete a file \n\tW -> Write(append) in file \n\tR -> Read the file \n\tE -> Exit \n\t>>> "))
    if choice.capitalize()=="C":
        inp=str(input("Enter name of file : "))
        file=open(inp,'x')
        file.close()
    
    elif choice.capitalize()=="D":
        import os
        x=str(input("Enter a file name : "))
        if os.path.exists(x) :
            os.remove(x)
            print("\n\nFile DELETED!!!\n\n")

        else:
            print(x)
    
    elif choice.capitalize()=="W":
        file=open(str(input("Enter a file name : ")),"a")
        file.write(str(input("Enter string to add in file : ")))
        file.close()
    
    elif choice.capitalize()=="R":
        file=open(str(input("Enter a file name : ")),"r")
        print(file.read())
        file.close()
    
    elif choice.capitalize()=="E":
        x=False
    
    else:
        print("Enter A Valid Choice")