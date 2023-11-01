# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200,’d’:400} 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400} 


# d1.update(d2)
for i in d1.keys():
    for j in d2.keys():
       
       i+j
print(d1)