import math

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "division by zero is not allowed"
    else:
        return a / b
    
def modulo(a, b):
    if b == 0:
        return "modulo by zero is not allowed"
    else:
        return a % b
    
def exponentiate(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "square root of a negative number is not defined"
    else:
        return math.sqrt(a)

history = []
while True:
  print("select the operation you want to perform: ")
  switch = input("1. addition\n2. subtraction\n3. multiplication\n4. division\n5. modulo\n6. exponentiation\n7. square root\n8. exit\n9. view history\n")

  if switch == '8':
    print("exiting the calculator...")
    break
  
  elif switch == '7':
        try:
          num1 = float(input("enter the number: "))
          if math.isnan(num1) or math.isinf(num1):
            raise ValueError("input cannot be NaN or infinity.")
        except ValueError:
            print("invalid input. please enter a valid number.")
            continue
        result = square_root(num1)
        history.append(f"sqrt({num1}) = {result}")
        print(result)
        with open("history.txt", "a") as file:
           file.write(f"sqrt({num1}) = {result}\n")
        
  elif switch in ['1', '2', '3', '4', '5', '6']:

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
      result = add(num1, num2)
      history.append(f"{num1} + {num2} = {result}")
      print(result)
      with open("history.txt", "a") as file:
         file.write(f"{num1} + {num2} = {result}\n")

    elif switch == '2':
      result = subtract(num1, num2)
      history.append(f"{num1} - {num2} = {result}")
      print(result)
      with open("history.txt", "a") as file:
         file.write(f"{num1} - {num2} = {result}\n")

    elif switch == '3':
      result = multiply(num1, num2)
      history.append(f"{num1} * {num2} = {result}")
      print(result)
      with open("history.txt", "a") as file:
         file.write(f"{num1} * {num2} = {result}\n")

    elif switch == '4':
      result = divide(num1, num2)
      history.append(f"{num1} / {num2} = {result}")
      with open("history.txt", "a") as file:
          file.write(f"{num1} / {num2} = {result}\n")
      print(result)

    elif switch == '5':
      result = modulo(num1, num2)
      history.append(f"{num1} % {num2} = {result}")
      with open("history.txt", "a") as file:
          file.write(f"{num1} % {num2} = {result}\n")
      print(result)

    elif switch == '6':
      result = exponentiate(num1, num2)
      history.append(f"{num1} ** {num2} = {result}")
      with open("history.txt", "a") as file:
          file.write(f"{num1} ** {num2} = {result}\n")
      print(result)

  elif switch == '9':
      if not history:
          print("no calculations yet.")
      else:
          print("calculation history:")
          for entry in history:
              print(entry)

  else:
    print("invalid input")



  

