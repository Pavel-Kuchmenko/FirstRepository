user_data = {"name":None, "surname":None}
print("--------------------------2-d task----------------------------")
print("Enter your name:")
user_data["name"] = input()
print("Enter your surname:")
user_data["surname"] = input()
print(f"Hi {user_data['name']} {user_data['surname']}!\n\n")
#----------------------------------------------------------------------
print("--------------------------1-st task---------------------------")
print("Lests start.")
print("Enter 3 integers:")
digits_list = [0, 0, 0]
digits_list[0], digits_list[1], digits_list[2] = int(input()), int(input()), int(input())
print(f"{digits_list[0]} + {digits_list[1]} = {digits_list[0]+digits_list[1]}")
print(f"{digits_list[1]} * {digits_list[2]} = {digits_list[1] * digits_list[2]}\n\n")
#----------------------------------------------------------------------
print("--------------------------3-rd task---------------------------")
print(f"{user_data['name']} {user_data['surname']} welcome to distance converter!")
distance: int = 0
print("Enter distance in meters:")
distance = int(input())
print(f"Distance in kilometers:{distance/1000}km\nDistance in milimeters:{distance*1000}mm\n")
print("-----------------------------END------------------------------")
