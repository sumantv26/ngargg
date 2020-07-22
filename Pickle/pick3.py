#! Reading Binary File

import pickle

f= open('students', 'rb')      
text= pickle.load(f)
# print("Name\tClass\tRoll Number")
# for i in range(len(text)):
#     for record in text:
#         print(record,end="\t")

# print("\n\n\n\t\t Thank You !!!")

print(text)