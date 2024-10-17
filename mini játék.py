class Warrior:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self,other_warior):
        other_warior -=  self.attack_power
        
    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
        

harcos_1 = Warrior("Bukvaktás",20,3)
harcos_2 = Warrior("Terbungos",22,2)
igaz_1 = harcos_1.is_alive()
igaz_2 = harcos_2.is_alive()
while igaz_1 == True or igaz_2 == True:
    print("rrrrr")
    print(harcos_1.attack(harcos_2.health))
    
    
