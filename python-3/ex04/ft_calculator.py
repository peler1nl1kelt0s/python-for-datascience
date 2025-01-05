class calculator:
    """
    Calculator class is to calculate a list.
    Functions:
        dotproduct : product whole list with another list
        add_vec : sum whole list with another list
        sous_vec : subtitude whole list with another list
    """
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(list(V1[i] * V2[i] for i in range(len(V1))))
        print(f"Dot product is: {result}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = list(float(V1[i] + V2[i]) for i in range(len(V1)))
        print(f"Add Vector is: {result}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = list(float(V1[i] - V2[i]) for i in range(len(V1)))
        print(f"Sous Vector is: {result}")
