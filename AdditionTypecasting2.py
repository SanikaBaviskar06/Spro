a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
sub = a - b
mul = a * b

print("Addition =", sum)
print("Subtraction =", sub)
print("Multiplication =", mul)


if b != 0:
    div = a / b
    print("Division =", div)
else:
    print("Division is not possible because second number is 0")