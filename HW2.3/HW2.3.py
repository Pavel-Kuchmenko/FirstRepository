from random import randint

list_1 = list()
list_2 = list()
#================================Creating two lists with randint()================================
for value in range(1, 11):
    list_1.append(randint(1, 50))
    list_2.append(randint(1, 50))
print(f"1-st list:{list_1} Length:{len(list_1)}\n")
print(f"2-nd list:{list_2} Length:{len(list_2)}\n")
#================Creating 3-rd list with two previous and removing repeated values================
print("=======Createng 3-rd list with two previous and removing repited values=======")
list_3 = list_1 + list_2
print(f"3-rd list with duplicates:{sorted(list_3)} Length:{len(list_3)}\n")
print("======================Removing duplicates from 3-rd list======================")
#===========================================My algorithm===========================================
buffer_list = list_3.copy()
for value in list_3:
    while value in buffer_list:
        buffer_list.remove(value)
    buffer_list.append(value)
list_3 = buffer_list.copy()
print(f"3-rd list with removed duplicates using algorithm:{sorted(list_3)} Lenght:{len(list_3)}\n")
#==============================================set()===============================================
del list_3
list_3 = set(list_1 + list_2)
print(f"3-rd list with removed duplicates using set():{sorted(list_3)} Lenght:{len(list_3)}\n")
#===================Createng 3-rd list with duplicated values from two previous====================
print("=========Createng 3-rd list with duplicated values from two previous==========")
del list_3
list_3 = list()
for value  in list_1:
    if value in list_2 and value not in list_3:
        list_3.append(value)
print(f"3-rd list with duplicated values from two previous: {list_3} Length:{len(list_3)}\n")
#=====================Createng 3-rd list with unique elements from two previous=====================
print("===========Createng 3-rd list with unique elements rom two previous===========")
del list_3
list_3 = list()
for value in list_1:
    if value not in list_2 and value not in list_3:
        list_3.append(value)
for value in list_2:
    if value not in list_1 and value not in list_3:
        list_3.append(value)
print(f"3-rd list with unique elements from two previous: {sorted(list_3)} Length:{len(list_3)}\n")
#====================Createng 3-rd list with max and min values of two previous====================
print("==========Createng 3-rd list with max and min values of two previous==========")
del list_3
list_3 = list()
list_1 = sorted(list_1)
list_2 = sorted(list_2)
list_3.extend((list_1[0], list_2[0], list_1[-1], list_2[-1]))
print(f"3-rd list with max and min values of two previous: {list_3}, Length:{len(list_3)}")
print("======================================END======================================")