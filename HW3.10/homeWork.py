from random import randint
from threading import Thread
from queue import Queue
from time import sleep


que = Queue()
##############################
def storeInQueque(func):     #
    def wrapper(*args):      # Decorator
        que.put(func(*args)) #
    return wrapper           #
##############################


@storeInQueque
def get_random_list() -> list[int]:
    print("1-st thread start.")
    delay(3)
    return [randint(1, 10) for _ in range(10)]


@storeInQueque
def get_sum_of_list_elements(received_list: list[int]) -> int:
    print("2-nd thread start.")
    delay(2)
    return sum(received_list)


@storeInQueque
def get_average_of_list_elements(received_list: list[int]) -> float:
    print("3-rd thread start.")
    delay(2)
    return sum(received_list)/len(received_list)


def delay(value: int) -> None:
    while value != 0:
        print(f"Delay:{value}")
        sleep(1)
        value-=1


def main() -> None:
    random_list = list()
    thread_list = [Thread(target=get_random_list), 
                   Thread(target=get_sum_of_list_elements, args=(random_list,)), 
                   Thread(target=get_average_of_list_elements, args=(random_list,))]  
    for index, value in enumerate(thread_list):
        if index == 0:
            value.start()
            value.join()
            random_list += que.get()
            continue
        value.start()
    result = [que.get(), que.get()]
    print(f"List sum: {result.pop() if result[-1] > result[0] else result.pop(0)}\n")
    print(f"List average: {result.pop()}\n")


if __name__ == '__main__':
    main()