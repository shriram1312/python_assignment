
# Write a Python function that takes a list of words and returns the length
# of the longest one

list=["karanwrhjfejrgkjkjfsvckjer","ashutoshu3jhrfjwfkj","bhavinjegwf","revese"]

list_word=""
list_length=0

for word in list:
    length=0
    for char in word:
        length+=1
        

    if length > list_length:
        list_length=length
        list_word=word

print("longest word:",list_word)
print("length of the word:",list_length)

