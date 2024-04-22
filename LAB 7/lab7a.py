def inputLength():
    return float(input("Enter the length: "))
length = inputLength()

def inputWidth():
    return float(input("Enter the width: "))
width = inputWidth()


def analyze(length, width):
    if length == width:
        print("It's a square")
    else:
        print("It's not a square")
analyze(length, width)


def compute(length, width):
    area = length * width
    return print("Area: " , int(area))
compute(length,width)