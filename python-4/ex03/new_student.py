import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    This function makes a 15 character id for a
    student member
    """

    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    This is a dataclass. Store variable without init
    function. And more readeble and the best one for
    if you wanna store data.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        Post init function calls when dataclass created.
        """
        self.login = self.name[0].capitalize() + self.surname.lower()
