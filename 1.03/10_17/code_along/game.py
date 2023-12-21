class Pokemon:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap
    
    def attack(self, other):
        other.hp -= self.ap
    def heal (self):
        self.hp += self.ap
        print ("current ")


pokA = Pokemon("charmander", 100, 20)
pokB = Pokemon("squirtle", 100, 30)
pokC = Pokemon("bulbasaur", 100, 26)

while True:
  pokA.attack(pokB)

        print(pokA.hp)
        print(pokB.hp)
        print(pokC.hp)

    if pokA.hp <= 0:
        print(f"{pokA.name} is dead")
        break
    elif pokB.hp <= 0:
        print(f"{pokB.name} is dead")
        break
    elif pokC.hp <= 0:
        print(f"{pokC.name} is dead")
        break
    else:
        print("Next Round")

print("You Won! you killed the pokemon...peta is coming")