import math
def add(a, b):
    result = a + b
    return result
def subtract(a, b):
    result  = a - b
    return result
def multiply(a, b):
    result  = a * b
    return result
def divide(a, b):
    if b == 0:
        return "division by zero is not allowed"
    else:
        return a / b


while True:
  print("select the operation you want to perform: ")
  switch = input("1. addition\n2. subtraction\n3. multiplication\n4. division\n5. exit\n")

  if switch == '5':
    print("exiting the calculator...")
    break

  try:
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    if math.isnan(num1) or math.isnan(num2) or math.isinf(num1) or math.isinf(num2):
        raise ValueError("input cannot be NaN or infinity.")
  except ValueError:
    print("invalid input. please enter valid numbers.")
    continue
  except Exception as e:
    print(f"an error occurred: {e}")
    continue

  if switch == '1':
    print(add(num1, num2))
  elif switch == '2':
    print(subtract(num1, num2))
  elif switch == '3':
    print(multiply(num1, num2))
  elif switch == '4':
    print(divide(num1, num2))
  else:
    print("invalid input")
  

