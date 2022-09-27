x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 #1
print(x)

students[0]["last_name"] = "Bryant" #2
print(students[0]["last_name"])

sports_directory["soccer"][0] = 'Andres' #3
print(sports_directory["soccer"][0])

z[0]['y'] = 30
print(z[0]['y']) 

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print(f'{"first_name"} - {students[i]["first_name"]}, {"last_name"} - {students[i]["last_name"]}')
        
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
        
# iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    # for each_key in dojo:
    #     print(f'{len(dojo[each_key])} {each_key.upper()}')
    #     for key in range(len(dojo[each_key])):
    #         print(dojo[each_key][key])
    
    for key, val in dojo.items():
        print(f'{len(val)} {key.upper()}')
        for i in range(0,len(val)):
            print(val[i])

printInfo(dojo)
    
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
