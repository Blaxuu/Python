from typing import Callable, Union, Mapping
from copy import copy, deepcopy
class Product:

    def __init__(self, id_:str, name:str , price:float) -> None:
        self.name = name
        self.id = id_
        self.price = price
    def __str__(self) -> str:
        return("<" + self.name +"> [<" + str(self.id) + ">] : $<" + str( '%.2f' % self.price) + ">")

    def __eq__(self, other) -> bool:
        if(self.id == other.id) and (self.name == other.name) and (self.price == other.price):
            return(True)
        return(False)



class Catalogue:
    Inventory = Mapping[str, Product]
    def __init__ (self, inventory :Inventory = None)->None:
        self.inventory = deepcopy(inventory) if inventory else {}

    def __contains__(self, id_: str) -> bool:
        return id_ in self.inventory

    def add_product(self, product : Product) -> None:
        self.inventory[product.id] = copy(product)



