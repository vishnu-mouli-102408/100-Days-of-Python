#  Calculator

print("Welcome to the Calculator");

def add(n1 ,n2):
    return n1 + n2
def subtract(n1 ,n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

num1 = float(input("Enter your first number: "))



for key in operations:
    print(key)

should_continue = True;

while should_continue:
    operation_symbol = input("Pick an operation from above: ")

    num2 = float(input("Enter your second number: "))
    calc = operations[operation_symbol]

    ans = calc(num1,num2)

    print(ans)

    if input("Type y to continue or type no to stop: ") == "y":
        num1 = ans
    else:
        should_continue = False

