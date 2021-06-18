import os
import platform
information = list()
information = [
    {"fullname":"John Devidson", "phone": "+14844458798", "email": "john_devidson@gmail.com", "position": "developer", "room": "1", "skype": "supejohn07"},
    {"fullname":"Max Bush", "phone": "+14842989330", "email": "maxbush@gmail.com", "position": "qa", "room": "2", "skype": "maximalmax882"},
    {"fullname":"Helena Miller", "phone": "+14842918795", "email": "helena_miller_work@gmail.com", "position": "project manager", "room": "3", "skype": "helenawork02"},
    {"fullname":"John Richer", "phone": "+16102458245", "email": "richerjohn@gmail.com", "position": "seo", "room": "4", "skype": "richricher777"}
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
print("Hello. This program contains information about company employees.")

while True:
    print("Choose one of available options:\n1 -> Show list\n2 -> Edit list\n3 -> Clear screen.\n4 -> Close program.")
    option = input("Enter option number: ")
#============================================================ Show List ============================================================
    if option == '1':
        Clear_screen()
        for value, n in zip(information, range(1, len(information)+1)):
            print(f"{n}.Full name: {value['fullname']}\tPhone: {value['phone']}\tEmail: {value['email']}\tPosition: {value['position']}\tRoom: {value['room']}\tSkype: {value['skype']}")
        del option
#============================================================ Edit List ============================================================
    elif option == '2':
        Clear_screen()
        print("Do you want edit existed value add new or delete?\n1 -> Add new.\n2 -> Edit existed value.\n3 -> Delete.")
        choice: str = input("Enter option number: ")
#======================================================= Edit List -> Add new ======================================================
        if choice == '1':
            information.append({"fullname": input("Enter full name: "), "phone":input("Enter phone: "), "email":input("Enter email: "), "position":input("Enter position: "), "room":input("Enter room: "), "skype":input("Enter skype: ")})
            del choice
#==================================================== Edit List -> Edit existed ====================================================   
        elif choice == '2':
            del choice
            for value, n in zip(information, range(1, len(information)+1)):
                print(f"{n}.Full name: {value['FullName']}\tPhone: {value['phone']}\tEmail: {value['email']}\tPosition: {value['position']}\tRoom: {value['room']}\tSkype: {value['skype']}")
            choice = input("Enter position number: ")
            information[int(choice)]["fullname"] = input("Old full name: "+information[int(choice)]["fullname"]+"\nEnter new full name: ")
            information[int(choice)]["phone"] = input("Old phone: "+information[int(choice)]["phone"]+"\nEnter new phone: ")
            information[int(choice)]["email"] = input("Old email: "+information[int(choice)]["email"]+"\nEnter new email: ")
            information[int(choice)]["position"] = input("Old position: "+information[int(choice)]["position"]+"\nEnter new position: ")
            information[int(choice)]["room"] = input("Old room: "+information[int(choice)]["room"]+"\nEnter new room: ")
            information[int(choice)]["skype"] = input("Old skype: "+information[int(choice)]["skype"]+"\nEnter new skype: ")
            del choice
#================================================ Edit List -> Delete position ====================================================           
        elif choice == '3':
            del choice
            for value, n in zip(information, range(1, len(information)+1)):
                print(f"{n}.Full name: {value['FullName']}\tPhone: {value['phone']}\tEmail: {value['email']}\tPosition: {value['position']}\tRoom: {value['room']}\tSkype: {value['skype']}")
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


