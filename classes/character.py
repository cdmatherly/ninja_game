class Character:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.health = 100
    
    def show_stats( self ):
        print(f"\nName: {self.name}\nStrength: {self.strength}\nHealth: {self.health}\n")
        return self

    def attack( self, target ):
        damage = self.strength
        print(f'\n[ATTACK] {self.name} attacks {target.name} for {damage}')
        target.defense(damage)
        return self
    
    def defense (self, damage):
        self.health -= damage
        print(f'\n[DEFENSE] {self.name} takes {damage} damage. Their health is now at {self.health}\n')