print("\"Homework #3\"\n05.06.2021\
      ")

print("--------------------------  START  -----------------------------")
integer1 = 300
integer2 = 55
float1 = 311.24
float2 = 575.59

result = 0
#--------------------------------------------------  **  ---------------------------------------------------------
print("----------------------------  **  ------------------------------")
print("_______Integers_______")
result = 3**4
print(3, 4, sep="\u002A\u002A", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Floats_______")
result = 3.4**4.
print(3.4, 4., sep="\u002A\u002A", end="="+str(result)+"\n")
print("Functions: bin(), oct() and hex() works only with integers. So we will use int() function to convert float to integer.")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Integer X Float_______")
result = 3**4.3
print(3, 4.3, sep="\u002A\u002A", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
#--------------------------------------------------  /  ---------------------------------------------------------
print("----------------------------  /  -------------------------------")
print("_______Integers_______")
result = integer1/integer2
print(integer1, integer2, sep="\u002F", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Floats_______")
result = float1/float2
print(float1, float2, sep="\u002F", end="="+str(result)+"\n")
print("Functions: bin(), oct() and hex() works only with integers. So we will use int() function to convert float to integer.")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Integer X Float_______")
result = integer1/float2
print(integer1, float2, sep="\u002F", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
#--------------------------------------------------  *  ---------------------------------------------------------
print("----------------------------  *  -------------------------------")
print("_______Integers_______")
result = integer1*integer2
print(integer1, integer2, sep="\u002A", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Floats_______")
result = float1*float2
print(float1, float2, sep="\u002A", end="="+str(result)+"\n")
print("Functions: bin(), oct() and hex() works only with integers. So we will use int() function to convert float to integer.")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Integer X Float_______")
result = integer1*float2
print(integer1, float2, sep="\u002A", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
#--------------------------------------------------  //  ---------------------------------------------------------
print("----------------------------  //  ------------------------------")
print("_______Integers_______")
result = integer1//integer2
print(integer1, integer2, sep="\u002F\u002F", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Floats_______")
result = float1//float2
print(float1, float2, sep="\u002F\u002F", end="="+str(result)+"\n")
print("Functions: bin(), oct() and hex() works only with integers. So we will use int() function to convert float to integer.")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Integer X Float_______")
result = integer1//float2
print(integer1, float2, sep="\u002F\u002F", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
#--------------------------------------------------  %  ---------------------------------------------------------
print("----------------------------  %  -------------------------------")
print("_______Integers_______")
result = integer1%integer2
print(integer1, integer2, sep="\u0025", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Floats_______")
result = float1%float2
print(float1, float2, sep="\u0025", end="="+str(result)+"\n")
print("Functions: bin(), oct() and hex() works only with integers. So we will use int() function to convert float to integer.")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("_______Integer X Float_______")
result = integer1%float2
print(integer1, float2, sep="\u0025", end="="+str(result)+"\n")
result = int(result)
print(bin(result).replace("0b", ""), end="->bin\n")
print(oct(result).replace("0o", ""), end="->oct\n")
print(hex(result).replace("0x", ""), end="->hex\n\n")
print("---------------------------  END  ------------------------------")