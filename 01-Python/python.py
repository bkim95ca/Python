#this is a single line comment

"""
This is a multiline comment
"""

# print("THIS IS HOW WE PRINT TO THE CONSOLE IN PYTHON")

# a = 7
# b = "hello world"
# c = True

#print(a,b,c)

x = 300
y = 300

if x < y:
    print(x, "is less than", y)
elif x > y:
    print(x, "is greater than", y)
else:
    print(x, "is equal to", y)
    

arr=["one", "two", "three", "four", "five", "six"]

for i in arr:
    print(i)
    

def callMessage():
    print("Hello Everyone! Python is awesome")
    

callMessage()