from unicodedata import name


dog = {
    'name' : 'Spot',
    'age' : '3',
    "color" : 'spotted',
    "favorite_food" : "cheese"
}

# for key in dog:
#     print(f"{key}: {dog[key]}")
#when loop over a dict, the iterative variable

#list of dicts
dog_list = [
    {
    'name' : 'Spot',
    'age' : '3',
    "color" : 'spotted',
    "favorite_food" : "cheese"
    },
    {
        'name' : 'Fido',
        'age' : 55,
        'color' : 'grey/white',
        'favorite_food' : 'applesauce and crickets'
    }
]

for dog in dog_list: 
    print(f'{dog["name"]}')
    for key in dog:
        print(f"{key}: {dog[key]}")
        
        
#while
i = 0
while i < 10:
    print(i)
    i+=1