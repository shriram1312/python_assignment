#  Write a Python program to split a list into different variables

list=[24,'tv','moible',200,'karan', 69,45.4]

int_values=[]
string_values=[]
float_values=[]


for values in list:
    if type(values) == int:
        int_values.append(values)
    elif type(values) == float:
        float_values.append(values)
    else:
        string_values.append(values)

print(int_values)
print(string_values)
print(float_values)


# from online

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)