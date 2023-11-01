# Write a Python program to unzip a list of tuples into individual lists. 

# test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
 
# # Printing original list
# print("Original list is : " + str(test_list))
 
# # using list comprehension to
# # perform Unzipping
# res = [[i for i  in test_list],
#        [j for j in test_list]]
 
# # Printing modified list
# print("Modified list is : " + str(res)) #data in list_of_tupl:
    

# Initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
 
# Printing original list
print("Original list is : " + str(test_list))
 
# Performing unzipping
# using zip() and * operator
res = list(zip(*test_list))
 
# Printing modified list
print("Modified list is : " + str(res))

