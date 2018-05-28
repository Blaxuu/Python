from typing import TypeVar, Container


class Movable:
    # TODO: zaimplementuj...
    pass


class Vehicle:
    def __init__(self, id_:str, brand:str):
        self.id = id_
        self.brand = brand
    def __str__(self)->str:
        return("<" + self.id + "> " + ":  " + "<" + self.brand +">")
    def max_speed(self)->float:
       pass


# TODO: Zmień wywołanie TypeVar() tak, aby 'V' był podtypem klasy 'Vehicle' (zob. parametr 'bound').
V = TypeVar('V')


def vehicle_collection_as_string(vehicles: Container[V]) -> str:
    raise NotImplementedError


class Car(Vehicle):
    def __init__(self, id_:str, brand:str, engine_hp:float):
        super().__init__(id_, brand)
        self.engine_hp=engine_hp
    def max_speed->float:
        return engine_hp
    pass


class Bicycle(Vehicle):
    def __init__(self,id_str, brand:str, n_gears:int):
        super().__init__(id_,brand)
        self.n_gears=n_gears
    def max_speed

    pass


def compute_min_travel_duration(distance: float, vehicle: Vehicle) -> float:
    raise NotImplementedError


def compute_min_travel_duration_as_string(distance: float, vehicle: Vehicle) -> str:
    raise NotImplementedError
