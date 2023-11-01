# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
# 300}, o {'item': 'item1', 'amount': 750}] 
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
       {'item': 'item1', 'amount': 750}]
dictionary={}
# print(data)
for values in data:
    for key,value in values.items():
        if key in dictionary:
            dictionary[key] += value
    else:
        dictionary[key] = value


        # print(key,value)
print(dictionary)