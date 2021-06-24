
#============================ Task #1 =============================
def show_message():
    tab = "\t"*6
    print("“Don't compare yourself with anyone in this world... if you do so, you are insulting yourself.”\n\n", tab, "Bill Gates")
#============================ Task #2 =============================
def show_even_numbers(value1, value2):
    buff = list()
    for value in range(value1+1, value2):
        if value%2 == 0:
            buff.append(value)
    print(f"Even numbers between {value1} and {value2}:\n{buff}")
    return
#============================ Task #3 =============================
def show_square(sign: str, square_size: int,  square_is_filled = False):
    space = ' '
    if  square_is_filled:
        for i in range(1, square_size+1):
            print(sign*square_size*2)
    else:
        for i in range(1, square_size+1):
            if i == 1 or i == square_size:
                print(sign*square_size*2)
            else:
                print(sign+space*(square_size-1)*2+sign)
#============================ Task #4 =============================        
def get_minimal_value(received_list: list):
    return print(f"Minimal value: {min(received_list)}")
#============================ Task #5 =============================
def get_multiplication_in_range(value1, value2):
    buff = 0
    if value1 > value2:
        value1, value2 = value2, value1
    for value in range(value1+1, value2):
        buff *= value
    print(f"Multiplication between {value1} and {value2}: {buff}")
    return buff
#============================ Task #6 =============================
def amount_of_numbers(number):
    print(f"Amount of numbers in reveived value: {len(str(number))}")
    return len(str(number))
#============================ Task #7 =============================
def is_value_palindrome(received_value):
    buff = str(received_value)[::-1]
    if str(received_value) == buff:
        return True
    return False
#========================= Try functions ==========================
print("==== Task #1 ====")
show_message()
print("==== Task #2 ====")
show_even_numbers(int(input("Show even numbers between two values.\nEnter 1-st value: ")), int(input("Enter 2-nd value: ")))
print("==== Task #3 ====")
show_square(input("Enter symbol for square: "), int(input("Enter square size: ")))
print("==== Task #4 ====")
get_minimal_value([int(input("Enter integer value: ")) for i in range(1, 6)])
print("==== Task #5 ====")
get_multiplication_in_range(int(input("Enter 1-st value: ")), int(input("Enter 2-nd value: ")))
print("==== Task #6 ====")
amount_of_numbers(int(input("Enter value:")))
print("==== Task #7 ====")
print(is_value_palindrome(int(input("Is value palindrome? Enter value: "))))
