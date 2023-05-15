from modules import *

class Trainer:
    def __init__(self, name) -> None:
        self.name = name
        self.list_objects = []
        self.list_weapons = []
        self.list_foods = []
        self.trainer_won = False
    def __repr__(self) -> str:
        return "Hi, my name is {} and I have {} objects, {} weapons and {} foods".format(self.name,len(self.list_objects), len(self.list_weapons), len(self.list_foods))
    
class Object:
    def __init__(self, name, pareq_x, pareq_y, pareq_z, limit_u, limit_v) -> None:
        self.name = name
        self.pareq_x = pareq_x
        self.pareq_y = pareq_y
        self.pareq_z = pareq_z
        self.limit_u = (u, limit_u[0], limit_u[1])
        self.limit_v = (v, limit_v[0], limit_v[1])
        self.volume = 0
        self.hp = 0
        self.base_attack = 0
        self.base_defense = 0
    def __repr__(self) -> None:
        sp.plotting.plot3d_parametric_surface(self.pareq_x,self.pareq_y,self.pareq_z,self.limit_u,self.limit_v, title=self.name)
    

class Weapon:
    def __init__(self, name, attack, defense, durability) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
        self.durability = durability

class Food:
    def __init__(self, name, hp_recovery) -> None:
        self.name = name
        self.hp_recovery = hp_recovery

#Test
Stefanny = Object('Stefanny', sp.cos(u + v), sp.sin(u - v), u - v, [-5,5], [-5,5])
print(Stefanny)