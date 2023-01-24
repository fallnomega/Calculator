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
    "*":"multiply",
    "/":"divide"
}

print(operations)

# num1 = int(input("Whats the first number?: "))
num1 = 3
# num2 = int(input("Whats the second number?: "))
num2 = 10

# math = input("What math operation did you want to perform with those two numbers? ( +, - , * , / ) :\n")
math = '+'
if math not in operations:
    print(f"{num1} {math} {num2} is not a valid math problem")
    exit()
results=0
if operations[math]=='add':
    result=add(num1,num2)
    print(result)
elif operations[math]=='subtract':
    result=subtract(num1,num2)
    print(result)
elif operations[math] == 'multiply':
    result=multiply(num1,num2)
    print(result)
else:
    result=divide(num1,num2)
    print(result)
