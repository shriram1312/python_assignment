
# Write a Python program to find whether a given number is even or odd,
# print out an appropriate message to the user.


from random import choice


status=True    # creating one status variable  and assigning value 

while status:    # initializing entry controlled condition statemnt
        num=int(input("enter any number to check whether it is EVEN or ODD:-\n"))  # creating one variable 
        if num%2==0:  # creating if condition statement
            print("it is EVEN numbe....\n")
            user=input(("do you want to check more number 'Y' or 'N':-")).upper()
            if user=="Y":     # creating nested if condition statement
                status=True
            else:
                status=False
                print("thank you")
        else:               # creating else condition statement
            print("it is ODD number.....")
            user=input(("do you want to check more number 'Y' or 'N':-")).upper()
            if user=="Y":    # creating another nested if condition statement
                status=True
            else:
                status=False
                print("thank you")

