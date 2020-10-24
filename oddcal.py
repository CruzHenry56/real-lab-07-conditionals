numone = int(input("Please give me a number "))
numtwo = int(input("Please give me another number "))
oper = input("What opertation would you like to use mul,div,mod ")

if (oper == "mul"):
    print(numone * numtwo)
elif (oper == "div"):
    print(numone / numtwo)
elif (oper == "mod"):
    print(numone % numtwo)
else:
    print("Invalid Operation")
