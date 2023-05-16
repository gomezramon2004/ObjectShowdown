from modules import *

class Trainer:
    def __init__(self, name) -> None:
        self.name = name
        self.list_objects = []
        self.list_weapons = []
        self.list_foods = []
        self.trainer_won = False
    def __repr__(self) -> str:
        return "Hi, my name is {} and I have {} objects, {} weapons and {} foods\n\t * Weapon: {} \n\t * Food: {}".format(self.name,len(self.list_objects), len(self.list_weapons), len(self.list_foods), self.list_weapons, self.list_foods)
    def create_object(self, name, entity, color) -> None:
        self.list_objects.append(Object(name,entity,color))
    def magic_roulette(self) -> None:
        self.list_weapons.append(weapons_list[randint(0,2)])
        self.list_foods.append(food_list[randint(0,2)])
    
class Object:
    def __init__(self, name, entity, color) -> None:
        self.name = name
        self.entity = entity
        self.color = color
        self.surfaceArea = entity.surfaceArea
        self.volume = entity.volume
        self.hp = 0
        self.base_attack = self.hp / entity.surfaceArea
        self.base_defense = self.hp / entity.volume
        self.weapon = None
    def __repr__(self) -> None:
        self.entity.ax.plot_superface(self.entity.x,self.entity.y,self.entity.z)
        plt.show()

class Sphere:
    def __init__(self, ratio, theta, phi) -> None:
        self.ratio = ratio
        self.theta = theta
        self.phi = phi
        theta, phi = np.meshgrid(theta, phi)
        self.x = ratio * np.sin(phi) * np.cos(theta)
        self.y = ratio * np.sin(phi) * np.sin(theta)
        self.z = ratio * np.cos(phi)
        self.surfaceArea = 4 * np.pi * ratio**2
        self.volume = (4/3) * np.pi * ratio**3
        fig = plt.figure()
        ax = Axes3D(fig)

class Weapon:
    def __init__(self, name, attack, defense, durability) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
        self.durability = durability
    def __repr__(self) -> str:
        return 'Name: {} | Attack: {} | Defense: {} | Durability: {}'.format(self.name,self.attack,self.defense,self.durability)

class Food:
    def __init__(self, name, hp_recovery) -> None:
        self.name = name
        self.hp_recovery = hp_recovery
    def __repr__(self) -> str:
        return 'Name: {} | HP Recovery: {}'.format(self.name,self.hp_recovery)

#List Of Weapons and Food
weapons_list = [Weapon('Sword',3,5,5), Weapon('Axe',7,2,6), Weapon('Whip',5,4,3)]
food_list = [Food('Apple',4), Food('Meat',6), Food('Cookie',2)]

#Debug
trainer1 = Trainer('Ramon')
trainer1.create_object('Sphery',Sphere(np.sqrt(4), np.arange(0, 2*np.pi, 0.01), np.arange(0, np.pi, 0.01)),'Green')
trainer1.magic_roulette()
print(trainer1)