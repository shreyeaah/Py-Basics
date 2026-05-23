num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print("select the operation you want to perform: ")

switch = input("1. addition\n2. subtraction\n3. multiplication\n4. division\n")
if switch == '1':
    print(num1 + num2)
elif switch == '2':
    print(num1 - num2)
elif switch == '3':
    print(num1 * num2)
elif switch == '4':
    if num2 == 0:
        print("division by zero is not allowed")
    else:
        print(num1 / num2)
else:
    print("invalid input")
