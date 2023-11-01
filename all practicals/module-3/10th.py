# Write a Python program to find the second smallest number in a list

nums = [2,4,6,54,33,44,33,6,0,2]
sm=float('inf')
ssm=float('inf')

# min=min(list)
# max=max(list)
# sum=sum(list)

# print(min)
# print(max)
# print(sum)

for num in nums:

    if num <= sm:
        sm,ssm = num,sm
    
    elif num < ssm:
        ssm = num

print (sm)
print(ssm)
    