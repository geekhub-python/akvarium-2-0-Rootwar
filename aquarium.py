from singleton import Singleton

class Auqarium(metaclass=Singleton):
    def __init__(self, max_residents):
        self.max_residents = max_residents
        self.current_auqarium = []

    def add_resident(self, resident):
        self.current_auqarium.append(resident)