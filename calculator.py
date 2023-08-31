"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Replace this with your code

sign = ""

while sign != "q":

    user_input = input(" > ")
    token = user_input.split(" ")

    sign = token[0]
    num1 = int(token[1])

    if len(token) > 2:
        num2 = int(token[2])

    if sign == "+":
        print(add(num1, num2))
    
    elif sign == "-":
        print(subtract(num1, num2))

    elif sign == "*":
        print(multiply(num1, num2))

    elif sign == "/":
        print(divide(num1, num2))

    elif sign == "square":
        print(square(num1))

    elif sign == "cube":
        print(cube(num1))

    elif sign == "pow":
        print(power(num1, num2))

    elif sign == "mod":
        print(mod(num1, num2))  

    