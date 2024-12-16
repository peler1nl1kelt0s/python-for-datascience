def NULL_not_found(obj: any) -> int:
    try:
        if obj is None:
            print(f"Nothing: {obj} <class '{type(obj).__name__}'>")
        elif obj != obj:
            print(f"Cheese: {obj} <class '{type(obj).__name__}'>")
        elif obj == 0 and type(obj) == int:
            print(f"Zero: {obj} <class '{type(obj).__name__}'>")
        elif obj == '' and type(obj) == str:
            print(f"Empty: {obj} <class '{type(obj).__name__}'>")
        elif obj is False and type(obj) == bool:
            print(f"Fake: {obj} <class '{type(obj).__name__}'>")
        else:
            print("Type not Found")
            return 1
        return 0
    except:
        print("Error")
        return 1
