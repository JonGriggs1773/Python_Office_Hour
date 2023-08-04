from wizard import Wizard
from weapon import Weapon
from fighter import Fighter


# gandalf = Wizard("Gandalf", "8ft", "Scrawny/Lean", "Fireball")
# dumbleduff = Wizard("Dumbledore", "9ft", "Old", "Elder Wand", "Avada Kedavra")

# for i in range(26):
#     gandalf.cast(dumbleduff)
#     dumbleduff.cast(gandalf)

michelangelo = Fighter("Mikey", "6ft", "Turtle Bro")
print(michelangelo.weapon)
nunchucks = Weapon("Nunchucks", 20)
print(nunchucks.type)




michelangelo.weapon = nunchucks
print(michelangelo.weapon.damage)