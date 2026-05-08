print("""Welcome to Python Calculator !
this can do basic operations like add subtract multiply and divide on any two digits""")

def calculate():
    num1 = float(input("first number : "))
    operation = input("The operation you want to do +, -, *, / : ")
    num2 = float(input("second number : "))
    
    if operation == "+":
        print(f"the answer of your operation {num1} {operation} {num2} is {num1 + num2}")

    elif operation == "-":
        print(f"the answer of your operation {num1} {operation} {num2} is {num1 - num2}")

    elif operation == "*":
        print(f"the answer of your operation {num1} {operation} {num2} is {num1 * num2}")

    elif operation == "/":
        if num2 == 0:
            print("division by zero isnt possible !")
        else:
            print(f"the answer of your operation {num1} {operation} {num2} is {num1 / num2}")
        

    else:
        print("try again !")

while True:
    calculate()