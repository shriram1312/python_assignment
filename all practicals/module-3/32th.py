# Write a Python program to map two lists into a dictionary

keys = ['red', 'green', 'blue','black']
values = ['#FF0000','#008000', '#0000FF','']

color_values=dict(zip(keys,values))  # zip() function can be used to store the data of list into a dictionary

print(color_values)