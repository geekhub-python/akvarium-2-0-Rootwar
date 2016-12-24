from singleton import Singleton

class Auqarium(metaclass=Singleton):
    MIN_RESIDENTS = 20
    MAX_RESIDENTS = 100

    def __init__(self, quantity_residents):
        if quantity_residents < Auqarium.MIN_RESIDENTS:
            raise Exception('Please enter quantity more {0}'.format(Auqarium.MIN_RESIDENTS))

        elif quantity_residents > Auqarium.MAX_RESIDENTS:
            raise Exception('Please enter quantity less {0}'.format(Auqarium.MAX_RESIDENTS))

        self.quantity_residents = quantity_residents
        self.current_auqarium = []

    def add_resident(self, resident):
        self.current_auqarium.append(resident)
