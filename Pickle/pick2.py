#! Pickle Update
import pickle

ch='Y'
while ch.upper()=='Y':
    name=str(input("Enter Name : "))
    sclass=str(input("Enter Class : "))
    rollno=str(int(input("Enter Roll Number : ")))
    f=open("students","ab")
    pickle.dump([name,sclass,rollno],f)
    f.close()
    print("File Appended Succesfully")
    ch=str(input("Do you want to enter more records (y for Yes) : "))

if ch.lower!="y" :
    print("\n\n\n\t\tThank You")