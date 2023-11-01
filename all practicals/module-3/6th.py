# Write a Python program to generate and print a list of first and last 5
# elements,  where the values are square of numbers between 1 and 30.

# import random
# list=[]
# for numbers in range(1,16):
        
#         com=random.randint(1,30)
#         list.append(com)

# print(list)

# print(list[:6],list[-6:])

list=[]
for value in range(1,31):

    value=value*value
    print(value,end=" , ")
    list.append(value)

print("\n")
print(f"first five value from list are : {list[:5]}")
print(f"last five value from list are : {list[-5:]}")

