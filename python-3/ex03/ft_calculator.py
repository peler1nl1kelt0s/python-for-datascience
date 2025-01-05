class calculator:
    """
    Calculator class is to calculate a list.
    Arguments:
        object: A list
    Functions:
        add : add whole list with a number
        mul : multiple whole list with a number
        sub : subtitude whole list with a number
        truediv : divide whole list with a number
    """
    def __init__(self, object: list):
        self.object = object

    def __add__(self, object) -> None:
        self.object = [i + object for i in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        self.object = [i * object for i in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        self.object = [i - object for i in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        if (object == 0):
            print("You can not divide with zero!")
            return
        self.object = [i // object for i in self.object]
        print(self.object)
