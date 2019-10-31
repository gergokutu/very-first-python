# ## Building a basic calculator
# # By default the input is string
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# # string to int / float
# # result = int(num1) + int(num2)
# # To be able to input decimals
# result = float(num1) + float(num2)

# print(result)

## Better calculator
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "*":
  print(num1 * num2)
elif operator == "/":
  print(num1 / num2)
else:
  print("Invalid operator")
