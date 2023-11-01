# Write a Python program to check multiple keys exists in a dictionary


names = { "karan" : 23, "kishan" : 28,"ronak" :34}

key=0

for keys in names.keys():
    key+=1

if  key>1:
    print("yes multiple keys dose exist in dictionary")
    print(f"there are {key} keys in dictionary right now")
    print(names.keys())
    
else:
    print("no multiple keys dose not exist in dictionary")
