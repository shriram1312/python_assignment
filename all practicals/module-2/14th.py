#Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string

str1="hello"
str2="karan"

print(str1+" "+str2)

print(str1[:2]+str2[:2]+" "+str2[:2]+str1[:2])
print(str2[:2]+str1[:2])

