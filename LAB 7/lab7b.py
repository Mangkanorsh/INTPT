firstNumber = float(input("Enter the First Number: "))
secondNumber = float(input("Enter the Second Number: "))

def intSum(int1,int2):
    total = int(int1) + int(int2)
    return  print("Sum: ", total)
intSum(firstNumber, secondNumber)

def intDiff(int1,int2):
    total = int(int1) - int(int2)
    return  print("Difference: ", total)
intDiff(firstNumber, secondNumber)

def intProd(int1,int2):
    total = int(int1) * int(int2)
    return  print("Product: ", total)
intProd(firstNumber, secondNumber)

def intQuo(int1,int2):
    total = int(int1) / int(int2)
    return  print("Quotient: ", int(total))
intQuo(firstNumber, secondNumber)

def floatRem(int1,int2):
    total = int1 % int2
    return  print("Remainder: ", total)
floatRem(firstNumber, secondNumber)

