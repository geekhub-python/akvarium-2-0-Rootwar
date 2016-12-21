#Decorator for eating
def sad_prey(func):
    def wrapper(self, prey):
        cls_type = prey.__class__.__name__

        if cls_type != 'PredatorFish' and cls_type != 'Snail':
            return func(self, prey)
        else:
            return False
    return wrapper