

# Write a Python function to reverse a string if its length is a multiple of 4

str=input("enter any string:")

#print(str)
print("\n")



if (len(str))%4==0:
        for reverse in str[::-1]:
         print(reverse,end=" ")
else:
        print(str)


print("\n")


