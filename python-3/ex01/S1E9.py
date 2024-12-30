from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class representing a character in a story."""

    @abstractmethod
    def __init__(self, name: str, is_alive : bool = True):
        """
        Constructor for Character.

        :param first_name: The first name of the character.
        :param is_alive: Boolean representing if the character is alive. Defaults to True.
        """
        self.first_name = name
        self.is_alive = is_alive

    def die(self):
        """
        Change the character's health state to deceased.

        :return: None
        """
        self.is_alive = False

class Stark(Character):
    """A class representing a Stark family member."""
    def __init__(self, name, is_alive = True):
        """
        Constructor for Stark.

        :param first_name: The first name of the Stark family member.
        :param is_alive: Boolean representing if the Stark is alive. Defaults to True.
        """
        super().__init__(name, is_alive)