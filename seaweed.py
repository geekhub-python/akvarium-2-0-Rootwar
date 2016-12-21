from residents import Residents
from eating_decorator import sad_prey

class Seaweed(Residents):
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
        return 'I have eat oxygen'