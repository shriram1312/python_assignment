# Write a Python function that takes two lists and returns true if they have
# at least one common member. 
import random

list=[]
list1=[]
list2=[]
for i in range(0,20):
        com=random.randint(1,25)
        list.append(com)

list1=list[:10]
list2=list[10:]
# print(list1)
# print(list2)

for i in list1:
        print(i,end="  ")
print("\n")
for i in list2:
        print(i,end="  ")
print("\n")

# statuse=True

# while statuse:
for ele1 in list1:
                for ele2 in list2:
                        if ele1==ele2:
                                print(ele1)
                                break
                                break
                        
                        
                        # else:
                                # print("false")
                                # break




