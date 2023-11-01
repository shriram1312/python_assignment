# Write a Python function to check whether a number is in a given range


# def check(user):
#     list1=[]
#     for i in range(1,10):
#         list1.append(i)

#     if user in list1:
#         print("yes your number is in range")
#     else:
#         print("sorry your number is not in range")


# user=input("enter any number: ")
# check(user)

def test_range(n):
    if n in range(3,9):
        print(f" {n} is in the range")
    else :
        print("The number is outside the given range.")

# n=input("enter any number: ")
test_range(7)