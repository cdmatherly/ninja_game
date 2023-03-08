from classes.character import Character

class Ninja( Character ):

    def __init__( self , name ):
        super().__init__( name)
        self.name = name
        self.health = 100

    def quick_attack(self, target):
        damage = (self.strength - 4) * 3
        print(f'\n[QUICK ATTACK] {self.name} attacks {target.name} three times for {self.strength-4} damage each.')
        target.defense(damage)
        return self
    
    def heal(self):
        self.health += 10
        print(f'\n[ITEM: HEALTH POTION] {self.name} heals for 10hp. Their health is now {self.health}')
        return self