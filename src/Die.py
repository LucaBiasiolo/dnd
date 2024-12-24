import random

class Die:

    __quantity: int
    __type:int

    def __init__(self, quantity: int, type: int):
        self.__quantity = quantity
        self.__type = type

    def throw(self):
        result = 0
        for _ in range(self.__quantity):
            result += random.randint(1, self.__type)
        return result

    def __str__(self):
        return f"{self.__quantity}D{self.__type}"