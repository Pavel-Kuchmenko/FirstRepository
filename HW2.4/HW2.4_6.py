from random import randint

A = {1,2,3,4,5,6,7,8}
B = {22,2,24,16,66,71,22,4}
C = {0,2,12,17,26,22,1,24}
print(A)
print(B)
print(C)

print(f"Similar elements from all tuples:{A&B&C}")
print(f"Elemts that unique for every tuple:{A^B^C}")
print("Similar values at same positions:\t")

A = {1,2,3,4,5,6,7,8}
B = {22,2,24,16,66,71,22,4}
C = {0,2,12,17,26,22,1,24}

for value_a, value_b, value_c in zip(A,B,C):
    if value_a == value_b == value_c:
        print(value_a)