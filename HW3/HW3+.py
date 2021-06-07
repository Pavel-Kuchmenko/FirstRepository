#--------------------------------------------------  abs()  ---------------------------------------------------------
print("---------------------------------- abs() ---------------------------------")
print(abs(-1))
print(abs(-.6))
#-----------------------------------------------  ord(), chr()  ------------------------------------------------------
print("------------------------------ ord() chr() -------------------------------")
print("ord(%) = ", end="")
print(ord("%"))
print("chr(37) = ", end="")
print(chr(37))
#---------------------------------------------------  pow()  ----------------------------------------------------------
print("---------------------------------- pow() ---------------------------------")
print("5**2 = ", end=str(5**2)+"\n")
print("pow(5, 2) = ", end=str(pow(5,2))+"\n\n")
print("5**2 % 7 = ", end=str(5**2%7)+"\n")
print("pow(5,2,mod=7) = ", end=str(pow(5,2,mod=7))+"\n\n")
#---------------------------------------------------  ascii()  ---------------------------------------------------------
print("---------------------------------- ascii() --------------------------------")
print(ascii("a_b_¢_d"))
print("¢ - is not supported by ASCII!")
#---------------------------------------------------  bool()  ----------------------------------------------------------
print("---------------------------------- bool() ---------------------------------")
print("bool(1<2) = ", end=str(bool(1<2))+"\n")
print("bool(1>2) = ", end=str(bool(1>2))+"\n")
#---------------------------------------------  int() float() str()  ----------------------------------------------------
print("--------------------------- bool() float() str() --------------------------")
print("int(4.2) = ", "type(int(4.2)) = ", sep=str(int(4.2))+"\t", end=str(type(int(4.2)))+"\n")
print("float(5) = ", "type(float(5)) = ", sep=str(float(5))+"\t", end=str(type(float(5)))+"\n")
print("str(54) = ", "type(str(54)) = ", sep=str(54)+"\t", end=str(type(str(54)))+"\n")
#---------------------------------------------------  format()  ---------------------------------------------------------
print("--------------------------------- format() --------------------------------")
print("\"Hello, {}!\".format(\"everybody\") = ", end=str("Hello, {}!".format("everybody"))+"\n")
print("\"{0}, {1}, {2}\".format(\"a\", \"b\", \"c\") = ", end=str("{0}, {1}, {2}".format("a", "b", "c"))+"\n")
print("\"{}, {}, {}\".format(\"a\", \"b\", \"c\") = ", end=str("{}, {}, {}".format("a", "b", "c"))+"\n")
print("\"{2}, {1}, {0}\".format(\"a\", \"b\", \"c\") = ", end=str("{2}, {1}, {0}".format("a", "b", "c"))+"\n")
print("\"{0}{1}{2}\".format(\"he\", \"ll\", \"o!\") = ", end=str("{0}{1}{2}".format("he", "ll", "o!"))+"\n")
print("Coordinates: {latitude}, {longitude}\".format(latitude=\'37.24N\', longitude=\'-115.81W\') = " , end=str("Coordinates: {latitude}, {longitude}".format(latitude='37.24N', longitude='-115.81W'))+"\n")
#---------------------------------------------------  complex()  ---------------------------------------------------------
print("--------------------------------- complex() --------------------------------")
print("complex(1, 2) = ", end=str(complex(1, 2)) + "\n")
x = complex(1, 2)
print("x = comlex(1, 2)")
print("x.imag = ", end=str(x.imag) + "\n")
print("x.real = ", end=str(x.real) + "\n")