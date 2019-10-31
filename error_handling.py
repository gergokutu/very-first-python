## Try - except block >> catching errors

# # Try the next line in different places
# # Inside the try-except is gonna be caught
# # value = 10/0

# try:
#   # value = 10/0
#   number = int(input("Enter a number: "))
#   print(number)
# # This except catches anything going wrong inside the block
# except:
#   print("Invalid input")

try:
  # Try >> value = 10/0
  value = 10/1
  number = int(input("Enter a number: "))
  print(number)
# Catching specific errors >> good practice
except ZeroDivisionError:
  print("Devided by zero")
# Storing the error as a variable
except ValueError as err:
  print(err)