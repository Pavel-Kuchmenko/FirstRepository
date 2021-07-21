class Device:
    def __init__(self, name : str, price : float, 
                 release_year : int, power : int,
                 color : str, material : str) -> None:
        self.__name = name
        self.__price = price
        self.__release_year = release_year
        self.__power = power
        self.__color = color
        self.__material = material

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return f"{self.__price}$"

    @property
    def release_year(self):
        return self.__release_year

    @property
    def power(self):
        return f"{self.__power}W"

    @property
    def color(self):
        return self.__color

    @property
    def material(self):
        return self.__material
