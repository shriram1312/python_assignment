# Write a Python program to get the Factorial number of given number.
# Fibonacci Sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21,.......


num=int(input("enter any number to get Fibonacci swquence:-"))


A=0
B=1
print(A)
print(B)

for i in range (0,num,):
    C=A+B
    print(C)
    A=B
    B=C


