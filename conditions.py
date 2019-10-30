## If statement
# basic
is_male = False # change it to False and run
is_tall = False # change it to False and run

# : and indentation%, (), and/or...
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