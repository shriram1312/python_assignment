
#  Write a Python program to check whether an element exists within a tuple


tuple = (1, 2, 3, 4, 5)


for i in tuple:
    user= int(input("enter any number between 1 to 10 to chech wether it is available in tuple or not :"))

    if user in tuple:
        print(user)
        print("is available in tuple ")
        break
    else:
        print("sorry it is not available in tuple")
        break

