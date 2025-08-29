class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"Hi, I am {self.name} from {self.city}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.flying_speed = flying_speed

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flying_speed} km/h using {self.power}!")

class StrongHero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.strength_level = strength_level

    def use_power(self):
        print(f"{self.name} lifts massive objects with strength level {self.strength_level} using {self.power}!")
hero1 = FlyingHero("SkyRider", "Wind Control", "Metropolis", 300)
hero2 = StrongHero("MightyMax", "Super Strength", "Gotham", 95)

# Call methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
