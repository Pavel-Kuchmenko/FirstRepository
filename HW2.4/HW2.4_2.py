import os
import platform
information = list()
information = [
    {"english":"print", "russian": "печатать"},
    {"english":"input", "russian": "ввод"},
    {"english":"system", "russian": "система"},
    {"english":"release", "russian": "выпускать"}
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
print("Hello. This program contains english words with translation to russian.")

while True:
    print("Choose one of available options:\n1 -> Show list\n2 -> Edit list\n3 -> Clear screen.\n4 -> Close program.")
    option = input("Enter option number: ")
#============================================================ Show List ============================================================
    if option == '1':
        Clear_screen()
        for value, n in zip(information, range(1, len(information)+1)):
            print(f"{n}.English: {value['english']}\t->\tRussian: {value['russian']}")
        del option
#============================================================ Edit List ============================================================
    elif option == '2':
        Clear_screen()
        print("Do you want edit existed value add new or delete?\n1 -> Add new.\n2 -> Edit existed value.\n3 -> Delete.")
        choice: str = input("Enter option number: ")
#======================================================= Edit List -> Add new ======================================================
        if choice == '1':
            information.append({"english": input("Enter english word: "), "russian":input("Enter russian word: ")})
            del choice
#==================================================== Edit List -> Edit existed ====================================================   
        elif choice == '2':
            del choice
            for value, n in zip(information, range(1, len(information)+1)):
                print(f"{n}.English:{value['english']}\t->\tRussian:{value['russian']}")
            choice = input("Enter position number: ")
            information[int(choice)]["english"] = input("Old english word: "+information[int(choice)]["english"]+"\nEnter new english word: ")
            information[int(choice)]["russian"] = input("Old russian word: "+information[int(choice)]["russian"]+"\nEnter new russian word: ")
            del choice
#================================================ Edit List -> Delete position ====================================================           
        elif choice == '3':
            del choice
            for value, n in zip(information, range(1, len(information)+1)):
                print(f"{n}.English:{value['english']}\t->\tRussian:{value['russian']}")
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


