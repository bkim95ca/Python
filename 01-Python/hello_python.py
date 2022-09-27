print("Hello Class September 2022")

#VARIABLES

x=7
name_of_variable = 'in snake case'

#only class names will be capitalized
GLOBAL_VAR = 'this is a global variable'

# DATA TYPES


# PRIMITIVE
# number
num = 7
num = 9.3

# string
string ="this is my string"
string2 = 'this is my string2'

# boolean
# True or false value
bool = True
bool2 = False


# COMPOSITE
# lists (aka arrays in JS)
list = [1,2,3,4,5,6]
list2 = ["bob", "kyle", "susan", "peter"]

name = list2[1]
# elements accessed by index
list[3] = 7
# print(list)
# grab the first three elements of the list
first_three = list[0:3]
last_number = list[-1:]
# print(first_three)
# print(last_number)
# list functions
# len()
# print(len(list))
# max() min()
# print(max(list2))
# methods of lists: 
# .sort() pop()
# list.sort(reverse = True)
# print(list)
# list2.sort()
# print(list2)
# list2.pop()
# print(list2)




# dictionaries (aka objects in JS)
# {}
dog = {
    'name': 'Spot',
    'age' : 3,
    'color' : 'spotted',
    'favorite_food' : 'puppaccino'
}
print(dog['name'])
dog['name'] = 'Tiger'
print(dog)

# print(dog.get("favorite_food", 'not found'))

#checking if keys exist in dictionaries
# if "favorite_food" in dog:
#     print('he has a fav')
# else: 
#     print('he does not')
# del dog['favorite_food']
# dog.clear()
# fav_food = dog.pop('favorite_food')
# .popitem() will remove last
print(dog)
# print(fav_food)

# tuples IMMUTABLE LIST
tuple = (1,2,3,4,5,6)
print(tuple[3])


# conditionals

# if
# else
# elif (else if)
# < > <= >= == != (not ==) or and

if 'age' not in dog:
    print("Dog doesn't have an age")
elif dog['age'] > 4:
    print("Dog is older than 4")
else: 
    print("Dog is less than 4")