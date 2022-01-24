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
