class Book:
    """
    Class that represents book

    Keyword arguments:
    name : str -- name of book (default None)
    release_year : int -- the year the book was released (default None)
    publisher : str -- name who publish book (default None)
    genre : str -- genre of book (default None)
    author : str -- authore of book (default None)
    price : float -- average price of book (default None)
    """

    def __init__(self, **kwargs) -> None:
        self.__name = kwargs.get("name", None)
        self.__release_year = kwargs.get("release_year", None)
        self.__publisher = kwargs.get("publisher", None)
        self.__genre = kwargs.get("genre", None)
        self.__author = kwargs.get("author", None)
        self.__price = kwargs.get("price", None)

    def __del__(self):
        print(f"Object Book was deleted!")

    def __str__(self, result = "") -> str:
        for key, value in self.__dict__.items():
            result += f"{key[7:].title()}: {value}\n"
        return result
    
    ######################### Properties #########################
    #--------------------------- Name ----------------------------
    def get_name(self):
        return f"Name of book: {self.__name}"

    def set_name(self, name):
        if type(name) != str:
            print("Wrong \"name\" value type")
            raise ValueError
        else:
            self.__name = name
    #----------------------- release_year ------------------------
    def get_release_year(self):
        return f"Book release year is: {self.__release_year}"

    def set_release_year(self, release_year):
        if type(release_year) != int:
            print("Wrong \"release_year\" value type")
            raise ValueError
        elif release_year < 0 or release_year > 2021:
            print("Impossible date!!")
            raise SyntaxError
        else:
            self.__release_year = release_year
    #------------------------ publisher ---------------------------
    def get_publisher(self):
        return f"Book publisher is: {self.__publisher}"

    def set_publisher(self, publisher):
        if type(publisher) != str:
            print("Wrong \"publisher\" value type")
            raise ValueError
        else:
            self.__publisher = publisher
    #--------------------------- genre -----------------------------
    def get_genre(self):
        return f"Genre of book is: {self.__genre}"

    def set_genre(self, genre):
        if type(genre) != float and type(genre) != int:
            print("Wrong \"genre\" value type")
            raise ValueError
        else:
            self.__genre = genre
    #---------------------------- author -----------------------------
    def get_author(self):
        return f"Book author is: {self.__author}"

    def set_author(self, author):
        if type(author) != str:
            print("Wrong \"author\" value type")
            raise ValueError
        else:
            self.__author = author
    #---------------------------- price -----------------------------
    def get_price(self):
        return f"Book price is: {self.__price}$"

    def set_price(self, price):
        if type(price) != float and type(price) != int:
            print("Wrong \"price\" value type")
            raise ValueError
        else:
            self.__price = price
    ##############################################################
    


if __name__ == '__main__':
    b = Book(name = "Fahrenheit 451", release_year = 1953, publisher = "Ballantine Books", genre = "Dystopian", author = "Ray Bradbury", price = 14.49)
    ############ Manual print using variable properties ###########
    print("#"*40, "Manual print using variable properties", b.get_name(), b.get_release_year(), b.get_publisher(), b.get_genre(), b.get_author(), b.get_price(), "\n", sep='\n')
    #################### Print using __str__ ######################
    print("#"*40, "Print with __str__", b, sep='\n')
    del b

pass
        