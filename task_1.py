#!/usr/bin/env python3

from random import randint
from functools import wraps
from abc import ABCMeta, abstractmethod

#Decorator for eating
def sad_prey(func):
    @wraps(func)
    def wrapper(self, prey):
        cls_type = prey.__class__.__name__

        if cls_type != 'PredatorFish' and cls_type != 'Snail':
            return func(self, prey)
        else:
            return False
    return wrapper


#Metaclass for creating Singleton, this is bad practice
class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.__instance


#Class for all residents in aquarium
class Residents(metaclass=ABCMeta):
    @abstractmethod
    def eat(self, prey):
        """Resident method eat"""

    @abstractmethod
    def get_weight(self):
        """Resident weight"""


class Snail(Residents):
    def __init__(self, weight):
        self.weight = weight
        self.prey_count = 0

    def get_weight(self):
        return self.weight

    @sad_prey
    def eat(self, prey):
        cls = prey.__class__.__name__

        if (cls == 'Seaweed'):
            self.weight += int(prey.get_weight())
            self.prey_count += 1

            return True

    def get_prey_count(self):
        return self.prey_count


class Seaweed(Residents):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    @sad_prey
    def eat(self, prey):
        return 'I have eat oxygen'


class Fish(Residents):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    @sad_prey
    def eat(self, prey):
        cls = prey.__class__.__name__

        if (cls != 'Fish'):
            self.weight += int(prey.get_weight())
            return True


class PredatorFish(Fish):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name
        self.prey_count = 0

    def get_weight(self):
        return self.weight

    @sad_prey
    def eat(self, prey):
        if (prey):
            self.weight += int(prey.get_weight())
            self.prey_count += 1
            return True

    def get_prey_count(self):
        return self.prey_count


class Auqarium(metaclass=Singleton):
    def __init__(self, max_residents):
        self.max_residents = max_residents
        self.current_auqarium = []

    def add_resident(self, resident):
        self.current_auqarium.append(resident)


if __name__ == '__main__':
    QUANTITY_RESIDENT = 50
    QUANTITY_FISH = 20
    QUANTITY_SNAIL = 10
    QUANTITY_SEAWEED = 20

    #new aquarium
    deep_house = Auqarium(QUANTITY_RESIDENT)

    #new predator fish
    bivis = PredatorFish(10, 'Bivis')
    bathed = PredatorFish(10, 'Bathed')

    #include fish in aquarium
    for fish in range(QUANTITY_FISH):
        deep_house.add_resident(Fish(randint(1, 9)))

    #include seaweed in aquarium
    for fish in range(QUANTITY_SEAWEED):
        deep_house.add_resident(Seaweed(randint(1, 3)))

    #include snail in aquarium
    for snail in range(QUANTITY_SNAIL):
        deep_house.add_resident(Snail(randint(1, 5)))

    #include predator fish in aquarium
    deep_house.add_resident(bivis)
    deep_house.add_resident(bathed)

    #let's start begin
    while len(deep_house.current_auqarium) > QUANTITY_SNAIL + 2:
        count = len(deep_house.current_auqarium)
        resident = deep_house.current_auqarium[randint(0, count - 1)]
        prey = deep_house.current_auqarium[randint(0, count - 1)]

        if resident != prey and resident.eat(prey):
            del deep_house.current_auqarium[deep_house.current_auqarium.index(prey)]

    #final result and winner predator fish
    if bivis.get_weight() > bathed.get_weight():
        print('Winner - Bivis', bivis.get_weight(), bivis.get_prey_count())
        print(bathed.name, bathed.get_weight(), bathed.get_prey_count())
    else:
        print('Winner - Bathed', bathed.get_weight(), bathed.get_prey_count())
        print(bivis.name, bivis.get_weight(), bivis.get_prey_count())

    print()

    # final result and winner snail
    for resident in deep_house.current_auqarium:
        if resident.__class__.__name__ == 'Snail':
            print('Snail', resident.get_weight(), resident.get_prey_count())