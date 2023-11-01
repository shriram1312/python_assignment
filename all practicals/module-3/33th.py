#  Write a Python program to combine two dictionary adding values for common keys. 

# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 


# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200,'d':400} 



# for key1 in d1:
#     if key1 in d2:
#       d1.values() + d2.values() #this wil not work

# print(d1)


dict1 = {'a': 100, 'b': 200, 'c':300} 
dict2 = {'a': 100, 'b': 200, 'd':300} 
 
 
# adding the values with common key
for value in dict1:
    # print(key)
    if value in dict2:
        dict1[value] = dict2[value] + dict1[value]

     
print(dict1)