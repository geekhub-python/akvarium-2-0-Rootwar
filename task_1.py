#!/usr/bin/env python3

from random import randint
from aquarium import Auqarium
from snail import Snail
from seaweed import Seaweed
from fish import Fish
from predator_fish import PredatorFish


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
for seaweed in range(QUANTITY_SEAWEED):
    deep_house.add_resident(Seaweed(randint(1, 3)))

#include snail in aquarium
for snail in range(QUANTITY_SNAIL):
    deep_house.add_resident(Snail(randint(1, 5)))

#include predator fish in aquarium
def add_predator():
    yield deep_house.add_resident(bivis)
    yield deep_house.add_resident(bathed)

next(add_predator())
next(add_predator())

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