from random import randint

def is_numeric_values_in_list(list:list):
    for value in list:
        if type(value) == int or type(value) == float:
            return True
    return False

def is_integer_values_in_list(list:list):
    for value in list:
        if type(value) == int:
            return True
    return False

# Task #1 ========= Multiply all list elements between themselves ==============
def multiply_list_elements(list:list):
    result:int = 1
    if not is_integer_values_in_list(list):
        return print("There is no integers in list!")   
    for value in list:
        if type(value) != int:
            continue
        result *= value
    return result

# Task #2 ================ Searching minimal value in list =====================
def get_min_list_value(list:list):
    if not is_numeric_values_in_list(list):
        return print("There is no integers or floats in list!")
    return min(list)

# Task #3 ============== Searching prime numbers in list =======================
def get_amount_of_list_prime_numbers(list:list, return_prime_numbers:bool = False):
    prime_numbers = []
    counter:int = 0
    if not is_integer_values_in_list(list):
        return print("There is no integers in list!")
    for value in list:
        if type(value) != int:
            continue
        for i in range(1, value+1):
            if value%i == 0:
                counter += 1
        if counter == 2:
            prime_numbers.append(value)
        counter = 0
    if return_prime_numbers:
        return len(prime_numbers), prime_numbers
    else:
        return len(prime_numbers)

# Task #4 ============= Delete integer value from list ========================
def delete_int_from_list(list:list, delete_value:int = 0):
    amount_of_deleted:int = 0
    if delete_value == 0:
        return print()
    if delete_value in list:
        for value in list:
            if value == delete_value:
                list.remove(value)
                amount_of_deleted += 1
    if amount_of_deleted == 0:
        return print("There is no such value in list!")
    return amount_of_deleted

# Task #5 ================= Unite two lists in one ============================
def unite_lists(list1:list, list2:list):
    return list1+list2

# Task #6 ========== Exponentate every numeric list element ===================
def exponentiation_list_elements(pow_value:int, list:list):
    result_list = []
    if not is_numeric_values_in_list(list):
        return print("There is no integers or floats in list!")
    for value in list:
        if type(value) != int and type(value) != float:# if not int or float -> skipp value
            continue
        result_list.append(value**pow_value)   
    return result_list

#==================================== Try functions ============================

list1 = list()
list2 = list()
[list1.append(randint(1,15)) for i in range(1, 11)]
[list2.append(randint(1,15)) for i in range(1, 11)]
print(f"1-st list: {list1}")
print(f"2-nd list: {list2}")

print(f"Task #1 -> Multiply all numerical values of list1 between themselves:\n\
List1: {list1}\nAnswer: {multiply_list_elements(list1)}")
print(f"Task #2 -> Searching minimal value in list2 if there is numerical values in list:\n\
List2: {list2}\nAnswer: {get_min_list_value(list2)}")
print(f"Task #3 -> Searching prime numbers in list1:\n\
List1: {list1}\nAnswer: {get_amount_of_list_prime_numbers(list1)}")
print(f"Task #4 -> Delete integer value from list2:\nList2: {list2}")
print(f"Answer: {delete_int_from_list(list2, delete_value=int(input(f'Enter value whitch you need to be deleted from List2:')))} elements deleted!")
print(f"Task #5 -> Unite two lists in one:\n\
List1: {list1}\nList2: {list2}\nAnswer: {unite_lists(list1, list2)}")
print(f"Task #6 -> Exponentate every numeric list1 element:\nList1: {list1}")
print(f"Answer: {exponentiation_list_elements(int(input('Enter expotentation value for List1 numeric elements:')),list1)}")

