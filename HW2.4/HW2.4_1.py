import os
import platform

information = list()
information = [
    {"name":"Magick Johnson", "height": "2.06m"},
    {"name":"Lebron James", "height": "2.06m"},
    {"name":"Kobe Bryant", "height": "1.98m"},
    {"name":"Kareem Abdul-Jabbar", "height": "2.18m"}
]
option: str = ''
#=================================================================
def Clear_screen():                     #=========================
    if platform.system() == "Darwin":   #=========================
        os.system('clear')              #=========================
    elif platform.system() == "Linux":  #=========================
        os.system('clear')              #= Clear screen method ===
    elif "Win" in platform.system():    #=========================
        os.system('cls')                #=========================
    else:                               #=========================
        pass                            #=========================
#=================================================================
print("Hello. This program contains names and height of famous basketball players.")

while True:
    print("Choose one of available options:\n1 -> Show list\n2 -> Edit list\n3 -> Clear screen.\n4 -> Close program.")
    option = input("Enter option number: ")
#============================================================ Show List ============================================================
    if option == '1':
        Clear_screen()
        for value, n in zip(information, range(1, len(information)+1)):
            print(f"{n}.Name:{value['name']}\tHeight:{value['height']}")
        del option
#============================================================ Edit List ============================================================
    elif option == '2':
        Clear_screen()
        print("Do you want edit existed value add new or delete?\n1 -> Add new.\n2 -> Edit existed value.\n3 -> Delete.")
        choice: str = input("Enter option number: ")
#======================================================= Edit List -> Add new ======================================================
        if choice == '1':
            information.append({"name": input("Enter name: "), "height":input("Enter height: ")})
            del choice
#==================================================== Edit List -> Edit existed ====================================================   
        elif choice == '2':
            del choice
            for value, n in zip(information, range(1, len(information)+1)):
                print(f"{n}.Name:{value['name']}\tHeight:{value['height']}")
            choice = input("Enter position number: ")
            information[int(choice)]["name"] = input("Old name: "+information[int(choice)]["name"]+"\nEnter new name: ")
            information[int(choice)]["height"] = input("Old height: "+information[int(choice)]["height"]+"\nEnter new height: ")
            del choice
#================================================ Edit List -> Delete position ====================================================           
        elif choice == '3':
            del choice
            for value, n in zip(information, range(1, len(information)+1)):
                print(f"{n}.Name:{value['name']}\tHeight:{value['height']}")
            choice = input("Enter position number to delete: ")
            if int(choice) >= len(information) or int(choice) < 0:
                print("Wrong number! Program will shut down.")
            else:
                del information[int(choice)]
            del choice
        else:
            print("Wrong number! Try one more time.")
#============================================================ Clear screen =============================================================
    elif option == '3':
        Clear_screen()
#============================================================ Close program ============================================================
    elif option =='4':
        quit()
#================================================================ Error ================================================================
    else:
        print("Wrong number! Try one more time.")


