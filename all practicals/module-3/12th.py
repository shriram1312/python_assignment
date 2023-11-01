# Write a Python program to check whether a list contains a sub list 


# main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # sub_list1 = [2, 3, 4]
# sub_list1 = [5, 6, 5, 8]

# status=True

# while status:

#         for values in main_list:
        
#             for values1 in sub_list1:
#                 if values1 in main_list:
#                      status=True
#                      print(f"{values1} is available in sublist")
#                 else:
#                      status=False

#             break

#         break

 

test_list = [5, 6, 3, 8, 2, 1, 7, 1]
sublist = [8, 20, 1] 

print("The original list : " + str(test_list))  # coverting list into sring for concating with string 


# Using loop + list slicing
res = False
for numbers in range(len(test_list) - len(sublist) ):
     print(numbers)
   
     if test_list[numbers: numbers + len(sublist)] == sublist:
        res = True
        break
 
# printing result
print("Is sublist present in list ? : " + str(res))
