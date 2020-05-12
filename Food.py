class Food:
    def __init__(self, name):
        self.name = name

    def message(self):
        print('Food is a life')

    def energy(self):
        raise NotImplementedError

    def __str__(self):
        return self.name


class Junk(Food):

    energy = 0;

    def __init__(self, name, energy):
        super().__init__(name)
        self.food = 'junk'
        self.energy = energy

    def message(self):
        print('Junk food is a short life, but very interesting')

    def energy(self):
        print(f'you have a lot ({self.energy}) of energy')


class Healthy(Food):
    energy = 0

    def __init__(self, name, energy):
        super().__init__(name)
        self.energy = energy

    def message(self):
        print('Healthy food is a long life, but boring')

    def energy(self):
        print(f'you have a little {self.energy} energy')


foods = [Healthy('Soya', 100), Junk('Cola', 1000),  Healthy('Apple', 150), Junk('Chips', 900)]

for food in foods:
    print(food)
    food.message()
    food.energy()
    print()
