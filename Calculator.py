# Program make a simple calculator

# This code adds two numbers
def add(x,y):
    return x + y
# This code multiplies two numbers
def multiply(x,y):
    return x * y
    # This code subtracts 2 number
def subtract(x,y):
    return x - y
# This code divides 2 numbers
def divide(x,y):
    return x / y
  # Done with that
print("Select an operation.")
print("1.Add")
print("2.Multiply")
print("3.Subtract")
print("4.Divide")
while True:
# Take input from the user
    choice = input("Enter a choice(1/2/3/4): ")
 # check if choice is one of the four options
    if choice in ('1','2','3','4'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
      elif choice == "2":
        print(num1, "*", num2, "=", multiply(num1, num2))
      elif choice == '3':
        print(num1, "-", num2,"=", subtract(num1, num2))
      elif choice == '4':
          print(num1, "/", num2, "=", divide(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
      next_calculation = input("Do you want to do another calculation?")
      if next_calculation == "no":
        break

    else:      
      print("invalid Input")
