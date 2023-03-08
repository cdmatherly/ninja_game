from classes.character import Character

class Pirate(Character):

    def __init__( self , name ):
        super().__init__(name)
        self.name = name
        self.strength = 15
        self.health = 100
    
    def cannon_ball(self, target):
        damage = (self.strength * 2)
        print(f'\n[CANNON STRIKE] {self.name} attacks {target.name} for {damage} damage.')
        target.defense(damage)
        return self
    
    def smoke(self):
        self.strength += 10
        print(f"\n[ITEM: SMOKES] {self.name} smokes for a buff of 10.")
        return self