# Write a Python program to sort three integers without using 
# conditional statements and loops.

num2=int(input("enter one number:"))
num1=int(input("enter one two:"))
num3=int(input("enter one three:"))

A=min(num1,num2,num3)
B=max(num1,num2,num3)
C=(num1+num2+num3)-A-B

print(f"sort of three integers:{A},{C},{B}")