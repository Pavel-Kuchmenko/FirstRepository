import parent_classes

class Dollars(parent_classes.Money):
    def __init__(self, name : str, amount : int, 
                 coins_amount : int, coin_name = "cent",) -> None:
        super().__init__(name, amount)
        self.__coins_amount = coins_amount
        self.__coin_name = coin_name

    def __repr__(self, result="") -> str:
        for index, value in self.__dict__.items():
            result += f"{index}: {value}\n"
        return result

    def __add__(self, value) -> float:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount + second_amount

    def __sub__(self, value) -> float:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount - second_amount

    def __mul__(self, value) -> float:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount * second_amount

    def __truediv__(self, value) -> float:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount / second_amount
    
    def __ge__(self, value) -> bool:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount >= second_amount

    def __lt__(self, value) -> bool:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount < second_amount

    def __gt__(self, value) -> bool:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount > second_amount

    def __le__(self, value) -> bool:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount <= second_amount

    def __eq__(self, value) -> bool:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount == second_amount

    def __ne__(self, value) -> bool:
        first_amount = self.amount + self.__convert_coins(coins=self.coins_amount)
        second_amount = value.amount + self.__convert_coins(value.coins_amount)
        return first_amount != second_amount

      
    @property
    def coin_name(self):
        return self.__coin_name

    @coin_name.setter
    def coin_name(self, value):
        if isinstance(value, str):
            self.__coin_name = value
        else: 
            print("Wrong type!")

    @property
    def coins_amount(self):
        return self.__coins_amount

    @coins_amount.setter
    def coins_amount(self, value):
        if isinstance(value, int):
            self.__coins_amount = value
        else:
            print("Wrong type!")

    def __convert_coins(self, coins, result=0):
        result = coins//100
        result += (coins%100)/100
        return result
    


def main():
    wallet_1 = Dollars(name="Dollar", amount=20, coins_amount=239)
    wallet_2 = Dollars(name="Dollar", amount=10, coins_amount=543)
    wallet_3 = Dollars(name="Dollar", amount=30, coins_amount=1270)

    print(wallet_1, wallet_2, wallet_3, sep="\n")

    print(f"{wallet_1 + wallet_2 = }")
    print(f"{wallet_3 - wallet_2 = }")
    print(f"{wallet_1 * wallet_2 = }")
    print(f"{wallet_1 > wallet_2 = }")
    print(f"{wallet_1 < wallet_2 = }")
    print(f"{wallet_1 == wallet_2 = }")
    print(f"{wallet_1 == wallet_1 = }")
    print(f"{wallet_1 != wallet_2 = }")

if __name__ == '__main__':
    main()