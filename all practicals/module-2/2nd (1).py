
# Write a Python program to get the Factorial number of given number.
# factorial = 5! = 5*4*3*2*1


num=int(input("enter any value:-"))  # vreating 'num' variable, it will take input from user

sum=1  # creating another variable and assigning value

for i in range(num,0,-1):  # initializing  for loop statement and assigning condition  
    sum=sum*i               # multiplaying sum value with i
    
print("factorial value is :-",sum) # print all value of sum 
