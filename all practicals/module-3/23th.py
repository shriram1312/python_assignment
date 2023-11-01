
# Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ()]

for i in tuple1:
    if len(i)==0:
        tuple1.remove(i)
print(tuple1)

