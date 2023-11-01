# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.

list=[]
count=0

status=True

while status:
    string=input("enter any string: ")
    list.append(string)
    choice=input("do you want to add more string, press 'Y' or 'N':").upper()
    if choice=='Y':
        status=True
    else:
         status=False
        

for elements in list:
    if len(elements)>=2 and elements[0]==elements[-1]:
        
        print(elements)
        count=count+1

    else:
        print("have not given proper name or number")

# count.count(list)
print("total string:",count)
# print(list)