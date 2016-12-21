from fish import Fish
from eating_decorator import sad_prey

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