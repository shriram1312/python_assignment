# Write a Python script to check if a given key already exists in a
# dictionary. 

dict = {'tv': '27000', 'mobile': '15000', 'laptop': '50000'}

# user = input("enter product name to check whether it is there in the dictinory or not: ")

# if user in dict:
#     print(f"Key exists in the dictionary. {user}")
# else:
#     print("Key does not exist in the dictionary.")

for keys in dict.keys():
    user = input("enter product name to check whether it is there in the dictinory or not: ")
    if user==keys:
        print("key dose exiseted in dictionary")
        print()
    else:
        print("sorry") 

# quiz={
 
#     1 : {
#         "que": "who is prime ministed of india",
#         "ans" : "narendra modi", 
#        },
#     14 :{
#         "que": "who is most popular cricketer",
#         "ans":"ms dhoini",
#     }    
        
#         }

# # print(quiz)

# print(quiz[1]["que"])

# print(quiz[14]["ans"])

# studnet = {


#     "name":"karan",
#     "subject":"python",
#     "score": 78


# }

# K=studnet.values()
# print(K)

# for k in studnet.keys():
    # print(k)


# for v in studnet.values():
#     print(v)


# l1=["tv","mobile","fridge"]
# l2=["25000","15000","45000"]

# name=input("enter product name:")

# index_number = l1.index(name)

# print(index_number)

# price_value = l2[index_number]

# print(f"{name}= Rs.{price_value}")
