from art import logo
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

def do_math_things(a):
    num3 = int(input("Whats the next number?: "))
    math2 = input("What  operation did you want to perform? :")
    new_calculation_function = operations[math2]
    new_result = new_calculation_function(a,num3)
    print (new_result)
    again = input(f"Keep going with previous value {new_result} or exit back to main prompt? y/n :").lower()
    if again == 'n':
        print ("Goodbye !")
        return
    else:
        do_math_things(new_result)


operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

print(logo)
keep_going=True
while keep_going == True:
    additional_math = True
    num1 = int(input("Whats the first number?: "))
    num2 = int(input("Whats the second number?: "))

    for x in operations:
        print (x)
    math = input("What math operation did you want to perform with those two numbers? See above symbol options:")
    if math not in operations:
        print(f"{num1} {math} {num2} is not a valid math problem")
        exit()
    calculation_function = operations[math]
    result = calculation_function(num1,num2)
    print (f"Result so far: {result}")
    continue_math = input("Continue with this same calculation or exit it? [y/n]").lower()
    if continue_math=='n':
        print("Exiting out of current calculation !")
    elif continue_math!='n' and continue_math !='y':
        print("I dont recognize that answer. Goodbye !")
        keep_going = False
    else:
        keep_going = do_math_things(result)
    direction = input("Move on to new calculation or exit out ? [y/n]: ").lower()
    if direction=='n':
        print("Exiting out of current calculation !")
        keep_going=False
    elif continue_math=='y':
        keep_going = True
    else:
        print("I dont recognize that answer. Goodbye !")
        keep_going = False

