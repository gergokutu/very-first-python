## If statement to decide
# basic
is_male = False # change it to False and run
is_tall = False # change it to False and run

# : and indentation, not(), and/or...
if is_male and is_tall:
  print("You are both male and tall")
# if is_male or is_tall:
#   print("You are a male or tall or both")
# elif >> else if, and not()...
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are short and not male")
else:
  print("You are either not male or not tall")

## If statements to compare
# Pass three numbers to the function
# It gives back the maximum number
def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

print(max_num(1, 6, 2))