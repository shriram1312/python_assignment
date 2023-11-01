
# Write a Python program to sum of three given integers. However, if 
#two values are equal sum will be zero

a=int(input("enter the value no.1:-"))
b=int(input("enter the value no.2:-"))
c=int(input("enter the value no.3:-"))

D=a+b+c      # creating one variable and assigning summation of a,b,c 

print("-----------------------")

if a==b or b==c or c==a:  # creating if statemnt and giving some condition to it
    print("your sum is ZERO....")  # if condition is true then this massage will be shown

else:   # or else this part will be execute
    print("sum of your all values are:-",D)


