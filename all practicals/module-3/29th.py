# Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15.


# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d)


d=dict()
for x in range(1,16):
    d[x]=x            # like this i can asseign for loop's value to the dictionary
    dict=x
print(dict)
print(d)

for keys in d.keys():
    print(keys, end=" ,")