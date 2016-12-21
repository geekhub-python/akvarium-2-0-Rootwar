from residents import Residents
from eating_decorator import sad_prey

class Fish(Residents):
    def __init__(self, weight):
        try:
            self.weight = int(weight)
        except ValueError:
            print('Resident weight must be a integer')
            raise SystemExit

    def get_weight(self):
        return self.weight

    @sad_prey
    def eat(self, prey):
        cls = prey.__class__.__name__

        if (cls != 'Fish'):
            self.weight += int(prey.get_weight())
            return True