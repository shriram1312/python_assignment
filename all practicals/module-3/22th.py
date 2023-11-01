# Write a Python program to find the repeated items of a tuple.

tuple=(1,2,3,4,5,6,2,4)

for number in tuple:
    if tuple.count(number)>1:
        print(f"{number} is more then two times in the list")
    else:
        print()