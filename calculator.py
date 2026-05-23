import math
class Calculator:
  def __init__(self):
    self.history = []
      # Load history from file at startup
    try:
      with open("history.txt", "r") as file:
        for line in file:
          self.history.append(line.strip())

    except FileNotFoundError:
      pass
  
  def save_to_history(self, entry):
    self.history.append(entry)
    with open("history.txt", "a") as file:
      file.write(entry + "\n")

  def validate_number(self, num):
    if math.isnan(num) or math.isinf(num):
      raise ValueError("Input cannot be NaN or infinity.")
    
  def add(self, a, b):
    return a + b
    
  def subtract(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    if b == 0:
        return "division by zero is not allowed"
    else:
        return a / b
    
  def modulo(self, a, b):
    if b == 0:
        return "modulo by zero is not allowed"
    else:
        return a % b
    
  def exponentiate(self, a, b):
    return a ** b

  def square_root(self, a):
    if a < 0:
        return "square root of a negative number is not defined"
    else:
        return math.sqrt(a)
    
  def show_history(self):
        if not self.history:
            print("No calculations yet.")
            return
        print("\nCalculation History:")
        for entry in self.history:
            print(entry)

  def get_single_number(self):

        try:
            num = float(input("Enter the number: "))
            self.validate_number(num)
            return num
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None
        
  def get_two_numbers(self):

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            self.validate_number(num1)
            self.validate_number(num2)

            return num1, num2

        except ValueError as e:
            print(f"Invalid input: {e}")
            return None, None

  def run(self):
    while True:
      print("select the operation you want to perform: ")
      switch = input("1. addition\n2. subtraction\n3. multiplication\n4. division\n5. modulo\n6. exponentiation\n7. square root\n8. exit\n9. view history\n")

      if switch == '8':
        print("exiting the calculator...")
        break
      
      elif switch == '7':
        num = self.get_single_number()

        if num is None:
          continue

        result = self.square_root(num)
        entry = f"sqrt({num}) = {result}"
        self.save_to_history(entry)
        print(result)

      elif switch == '9':
        self.show_history()

      elif switch in ['1', '2', '3', '4', '5', '6']:

        num1, num2 = self.get_two_numbers()
        if num1 is None or num2 is None:
          continue
        if switch == '1':
          result = self.add(num1, num2)
          entry = f"{num1} + {num2} = {result}"

        elif switch == '2':
          result = self.subtract(num1, num2)
          entry = f"{num1} - {num2} = {result}"

        elif switch == '3':
          result = self.multiply(num1, num2)
          entry = f"{num1} * {num2} = {result}"

        elif switch == '4':
          result = self.divide(num1, num2)
          entry = f"{num1} / {num2} = {result}"

        elif switch == '5':
          result = self.modulo(num1, num2)
          entry = f"{num1} % {num2} = {result}"

        elif switch == '6':
          result = self.exponentiate(num1, num2)
          entry = f"{num1} ** {num2} = {result}"

        self.save_to_history(entry)
        print(result)

      else:
        print("Invalid input")




calc = Calculator()
calc.run()

  
