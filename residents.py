from abc import ABCMeta, abstractmethod

# Class for all residents in aquarium
class Residents(metaclass=ABCMeta):
    @abstractmethod
    def eat(self, prey):
        """Resident method eat"""

    @abstractmethod
    def get_weight(self):
        """Resident weight"""