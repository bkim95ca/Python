class Pet:
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
    # implement the following methods:
    def sleep(self):
        self.energy += 25
        return self    
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
# noise() - prints out the pet's sound
    def noise(self, type):
        if type == 'cat':
            print("meow")
        elif type == 'dog':
            print("bark")
        elif type == 'horse':
            print("neigh")
