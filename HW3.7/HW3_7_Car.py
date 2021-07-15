class Car:
    """ 
    Class that represents Car.
    
    Keyword arguments:
    name : str -- name of car (default None)
    year_of_issue : int -- year in which the car was released (default None)
    manufacturer : str -- name of manufacturer (default None)
    engine_volume : float -- volume of engine (default None)
    color : str -- color of car (default None)
    price : float -- price of car (default None)
    """

    def __init__(self, **kwargs) -> None:
        self.__name = kwargs.get('name', None)
        self.__year_of_issue = kwargs.get('year_of_issue', None)
        self.__manufacturer = kwargs.get('manufacturer', None)
        self.__engine_volume = kwargs.get('engine_volume', None)
        self.__color = kwargs.get('color', None)
        self.__price = kwargs.get('price', None)

    def __del__(self):
        print(f"Object Car was deleted!")

    def __str__(self, result = "") -> str:
        for key, value in self.__dict__.items():
            result += f"{key[6:].title()}: {value}\n"
        return result

    ######################### Properties #########################
    #--------------------------- Name ----------------------------
    @property
    def name(self):
        return f"Name of car: {self.__name}"

    @name.setter
    def name(self, name):
        if type(name) != str:
            print("Wron \"name\" value type")
            raise ValueError
        else:
            self.__name = name
    #----------------------- year_of_issue -----------------------
    @property
    def year_of_issue(self):
        return f"Car release year is: {self.__year_of_issue}"

    @year_of_issue.setter
    def year_of_issue(self, year_of_issue):
        if type(year_of_issue) != int:
            print("Wron \"year_of_issue\" value type")
            raise ValueError
        elif year_of_issue < 1886 or year_of_issue > 2021:
            print("Impossible date!!")
            raise SyntaxError
        else:
            self.__year_of_issue = year_of_issue
    #----------------------- manufacturer -------------------------
    @property
    def manufacturer(self):
        return f"Car manufacturer is: {self.__manufacturer}"

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        if type(manufacturer) != str:
            print("Wron \"manufacturer\" value type")
            raise ValueError
        else:
            self.__manufacturer = manufacturer
    #------------------------ engine_volume ------------------------
    @property
    def engine_volume(self):
        return f"Engine volume of car is: {self.__engine_volume}"

    @engine_volume.setter
    def engine_volume(self, engine_volume):
        if type(engine_volume) != float and type(engine_volume) != int:
            print("Wron \"engine_volume\" value type")
            raise ValueError
        else:
            self.__engine_volume = engine_volume
    #---------------------------- color -----------------------------
    @property
    def color(self):
        return f"Car color is: {self.__color}"

    @color.setter
    def color(self, color):
        if type(color) != str:
            print("Wron \"color\" value type")
            raise ValueError
        else:
            self.__color = color
    #---------------------------- price -----------------------------
    @property
    def price(self):
        return f"Car price is: {self.__price}$"

    @price.setter
    def price(self, price):
        if type(price) != float and type(price) != int:
            print("Wron \"price\" value type")
            raise ValueError
        else:
            self.__price = price
    ##############################################################
    


if __name__ == '__main__':
    c = Car(name = "Volga GAZ-3110", year_of_issue = 1985, manufacturer = "GAZ", engine_volume = 2.5, color = "white", price = 8800)
    ############ Manual print using variable properties ###########
    print("#"*40, "Manual print using variable properties", c.name, c.year_of_issue, c.manufacturer, c.engine_volume, c.color, c.price, "\n", sep='\n')
    #################### Print using __str__ ######################
    print("#"*40, "Print with __str__", c, sep='\n')
    del c

pass 

