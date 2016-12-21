from residents import Residents
from eating_decorator import sad_prey

class Snail(Residents):
    def __init__(self, weight):
        try:
            self.weight = int(weight)
        except ValueError:
            print('Resident weight must be a integer')
            raise SystemExit
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