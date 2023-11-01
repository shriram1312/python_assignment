# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5

a=int(input("enter the value no.1:-"))   # creating one variable and taking integer value from user
b=int(input("enter the value no.2:-"))

if a==b or a+b==5 or a-b==5:   # initializing  if condition 
    print("TRUE")  # if condition is true then print this statement
else:   # or ealse this will shown
    print("FALSE")
