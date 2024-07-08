x = float(input("Enter number_1 : "))
y = float(input("Enter number_2 : "))
op = str(input("Enter the operation : "))

if op == '+':
    Sum = x + y
    print("Sum of", x, "and", y, " = ", Sum)

elif op == '-':
    diff = x - y
    print("Difference of", x, "and", y, " = ", diff)

elif op == '*':
    mul = x * y
    print("Multiple of", x, "and", y, " = ", mul)

elif op == "/":
    div = x / y
    print("Division of", x, "and", y, " = ", div)

elif op == "//":
    fDiv = x // y
    print("Floor Division of", x, "and", y, " = ", fDiv)

elif op == "**":
    exp = x ** y
    print(x, "raised to the power", y, " = ", exp)

else:
    print("The operator you entered is unknown to the program...")