from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon is a class that inherited from Character
    """
    def __init__(self, name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        """
        Constructor for Baratheon.

        :param first_name: The first name of the character.
        :param is_alive: Boolean representing if the character is alive.
        Defaults to True.
        :param family_name: The family name of the character.
        :param eyes: The eyes of the character.
        :param hairs: The hairs of the character.
        """
        super().__init__(name, is_alive)
        self.eyes = eyes
        self.family_name = family_name
        self.hairs = hairs

    def __str__(self):
        """
        this is a function that informing to everyone basicly
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        this is a function that informing to programmer basicly
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    Lannister is a class that inherited from Character
    Have a function create a object on class like classmethod
    """
    def __init__(self, name, is_alive=True, family_name="Lannister",
                 eyes="blue", hairs="light"):
        """
        Constructor for Lannister.

        :param first_name: The first name of the character.
        :param is_alive: Boolean representing if the character is alive.
        Defaults to True.
        :param family_name: The family name of the character.
        :param eyes: The eyes of the character.
        :param hairs: The hairs of the character.
        """
        super().__init__(name, is_alive)
        self.eyes = eyes
        self.family_name = family_name
        self.hairs = hairs

    def __str__(self):
        """
        this is a function that informing to everyone basicly
        """
        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        this is a function that informing to programmer basicly
        """

        return f"Vector: ('{self.first_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, name: str, is_alive: True):
        """
        this is a function that creates a new Lannister object on class
        thats why its called class method.
        """
        return cls(name, is_alive)
