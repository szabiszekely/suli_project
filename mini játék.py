class Warrior:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attacj(self,other_warior):
        other_warior.health -=  self.attack_power
        
    def is_alive(self,alive):
        if self.health <= 0:
            alive = False
        else:
            alive = True
            
            