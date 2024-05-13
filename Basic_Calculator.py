# Basic Calculator

def add(a, b):
    answer = a + b
    print(str(a)+ "+" +str(b)+ "=" +str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a)+ "-" +str(b)+ "=" +str(answer) + "\n")

def mult(a, b):
    answer = a * b
    print(str(a)+ "*" + str(b) + "=" + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a)+ "/" +str(b)+ "=" +str(answer) + "\n")

while True:
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")

    option = input("Select your option : " )

    if option == "a" or option == "A":
        print("Addition")
        a = int(input("First number : "))
        b = int(input("Second number : "))
        add(a, b)

    elif option == "b" or option == "B":
        print("Subtraction")
        a = int(input("First number : "))
        b = int(input("Second number : "))
        sub(a, b)

    elif option == "c" or option == "C":
        print("Multiplication")
        a = int(input("First number : "))
        b = int(input("Second number : "))
        mult(a, b)

    elif option == "d" or option == "D":
        print("Addition")
        a = int(input("First number : "))
        b = int(input("Second number : "))
        div(a, b)

    elif option == "e" or option == "E":
        print("**********Ended**********")
        quit()
        

    