#Write a Python program to compute the value of a specified principal 
#amount, rate of interest, and a number of years

principle_amount=int(input("Enter Principle amount :- "))
rate_of_intrest=int(input("Enter rate of intrest % :- "))
time_period=int(input("Enter time period in years :- "))

#adding formula of simple intrest to calculate simple interest

A=principle_amount*rate_of_intrest*time_period

simple_intrest=A/100

print(f"Simple Intrest = {principle_amount} * {rate_of_intrest} * {time_period} / 100 = {simple_intrest}")



