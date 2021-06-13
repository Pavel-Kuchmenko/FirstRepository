user_data = {"name":None, "surname":None}
#------------------------Say hello to new user---------------------------
print("--------------------------2-d task----------------------------")
print("------------------Say hello to new user-----------------------")
print("Enter your name:")
user_data["name"] = input()
print("Enter your surname:")
user_data["surname"] = input()
print(f"Hi {user_data['name']} {user_data['surname']}!\n\n")
#---------------------Get summ and multiplications-----------------------
print("--------------------------1-st task---------------------------")
print("---------------Get summ and multiplications-------------------")
print("Lests start.")
print("Enter 3 integers:")
digits_list = [0, 0, 0]
digits_list[0], digits_list[1], digits_list[2] = int(input()), int(input()), int(input())
print(f"{digits_list[0]} + {digits_list[1]} = {digits_list[0]+digits_list[1]}")
print(f"{digits_list[1]} * {digits_list[2]} = {digits_list[1] * digits_list[2]}\n\n")
#---------------Convert meters to kilometers and milimeters---------------
print("--------------------------3-rd task---------------------------")
print("---------Convert meters to kilometers and milimeters----------")
print(f"{user_data['name']} {user_data['surname']} welcome to distance converter!")
distance: int = 0
print("Enter distance in meters:")
distance = int(input())
print(f"Distance in kilometers:{distance/1000}km\nDistance in milimeters:{distance*1000}mm\n")
print("-----------------------------END------------------------------")
