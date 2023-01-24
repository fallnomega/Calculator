from art import logo
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b



operations ={
    "+":"add",
    "-":"subtract",
    "*":"multiple",
    "/":"divide"
}

print(operations)

num1 = int(input("Whats the first number?: "))

num2 = int(input("Whats the second number?: "))