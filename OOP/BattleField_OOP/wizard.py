from fighter import Fighter



class Wizard(Fighter):
    def __init__(self, name, height, build, type, spell):
        super().__init__(name, height, build, type)
        self.spell = spell

    def cast(self, enemy):
        print(f"{self.name} casts {self.spell}")
        super().attack(enemy)