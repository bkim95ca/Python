class Character:
    def __init__(self):
        self.health = 100
        self.level = 1
        self.strength = 10
        self.defense = 5
    
    def attack(self, target):
        print("attacking")
        target.defend(self.strength)
        return self
        
        
    def defend(self, damage):
        print("defending")
        actual_damage = damage - self.defense
        self.health -= actual_damage
        
    def heal(self):
        self.health += 3
        
    def print_info(self):
        print(f'health {self.health} strength {self.strength} level {self.level} defense {self.defense}')