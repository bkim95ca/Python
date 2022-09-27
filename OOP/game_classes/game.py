from character import Character
from pokemon import Pokemon
import random

bob = Character()
bulbasaur = Pokemon('grass', 50)

while(bob.health > 0 and bulbasaur.health > 0):
    response = input("You're bob, will you attack or defend? \n 1) Attack \n 2) Heal \n")
    if response == '1':
        bob.attack(bulbasaur)
    elif response == '2':
        bob.heal()
    else:
        print("Please pick a valid option")
        
    roll = random.randint(1,3)
    if roll == 1:
        bulbasaur.attack(bob)
        print('bulbasaur attacks')
    elif roll == 2:
        bulbasaur.heal()
        print('bulbasaur heals')
    elif roll == 3:
        bulbasaur.level_up()
        print('bulbasaur levels up')
    
    print("Bob: ")
    bob.print_info()
    print("Bulba")
    bulbasaur.print_info()