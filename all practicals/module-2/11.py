
# Write a Python program to count the number of characters (character
# frequency) in a string


string = input("enter sentence to count the number of characters:")
count = 0   #Counts each character except space.

for i in range(len(string)):

    if string[i] != ' ':
        count = count + 1      #Displays the total number of characters present in the given string.


print("Total number of characters in a string: ",count)
