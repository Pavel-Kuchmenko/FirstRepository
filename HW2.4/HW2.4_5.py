from pprint import pprint

A = {1, 2.2, 4, 10, 15}
B = {3, 4.2, 22, 15, 66}
C = {2, 2.2, 3.3, 66, 4}
print("Different values of sets: ")
pprint(A|B)

print("Similar values of sets:")
pprint(A|C)

print("Union of all sets:")
pprint(A.union(B,C))