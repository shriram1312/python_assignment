# Write a Python program to find the highest 3 values in a dictionary

dic={"karan": 30, "ashutosh": 20, "bhavin": 35, "smit": 40, "shivharsh": 10,"dinesh": 200,"ketan": 140,}
list=[]

for values in dic.values():
    list.append(values)

s=sorted(list)  # sorted function is used in for sort all integer values 
print(s[-3:])


