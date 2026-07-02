def add(x, y):
        return x + y

def sub(x, y):
        return x - y

def mul(x, y):
        return x * y

def div(x, y):
        return x / y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("What's your operation? (+, -, *, /): ")

if op == "+":
        print(add(num1, num2))
elif op == "-":
        print(sub(num1, num2))
elif op == "*":
        print(mul(num1, num2))
elif op == "/":
        print(div(num1, num2))


def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))


def even_or_odd(num):
    if num % 1 == 2:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2))