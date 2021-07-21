from parent_classes import Device 



class Coffee_Machine(Device):
    def __init__(self, name: str, price: float, 
                 release_year: int, power: int, 
                 color: str, material: str,
                 water_tank_capacity : float,
                 thermoblock : bool, auto_shut_off : bool,
                 variable_cup_size : list[str]) -> None:
        super().__init__(name, price, release_year, power, color, material)
        self.__water_tank_capacity = water_tank_capacity
        self.__thermoblock = thermoblock
        self.__variable_cup_size = variable_cup_size

    @property
    def water_tank_capacity(self):
        return self.__water_tank_capacity

    @property
    def thermoblock(self):
        return self.__thermoblock

    @property
    def variable_cup_size(self):
        return self.__variable_cup_size


class Blender(Device):
    def __init__(self, name: str, price: float, 
                 release_year: int, power: int, 
                 color: str, material: str) -> None:
        super().__init__(name, price, release_year, power, color, material)
        self.__




if __name__ == '__main__':

    coffe_variable_cup_size = ["40ml", "150ml", "230ml"]

    coffe = Coffee_Machine(name = "Nespresso", price = 60., 
                           release_year=2016, power=1280, 
                           color="black", material="metal", 
                           water_tank_capacity=1.2, thermoblock=True, 
                           auto_shut_off=False, variable_cup_size=coffe_variable_cup_size)

    blend = ...

    print(coffe.name)