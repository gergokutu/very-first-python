for i in range(5):
  print("Hello Mogyi! :) - written in Python3.8")

# Same with Javascript
# for (let i = 0; i < 5; i++) {
#   console.log("Let's start it! :) - written with vanillaJS")
# }

## Draw triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

## Variables >> only: variable_name = "value"
character_name = "Pocok"
# Not character_age = 35.5 >> cannot concatenate 'str' and 'int' objects...
character_age = "35.5"
# True needs to be capitol
# Not isMale but is_male
is_male = True 
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")

character_name = "Pista"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

## Working with strings
# Escape character >> \ << "\n"...
print("Pocok\nAcademy")
print("Pocok\"s Academy")

phrase = "Let's do it!"
phrase_two = "TWO"
# Concatenation >> +
print(phrase + " Now!!!")
# lower(), islower()...
print(phrase + " Now!!!".lower())
print(phrase.lower() + " Now!!!")
print(phrase.lower() + " NOOW!!!".lower())

print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase_two.isupper())

print(phrase_two.lower().islower())

# len >> lenght
print(len(phrase))

# Grab the first character
print(phrase[0])

# Grab the index
print(phrase.index("L"))
print(phrase.index("Let"))

# Replace do >> concatenate
print(phrase.replace("do", "concatenate"))

## Working with strings
# +, -, %, ... 

print(-2.01213)
print(3 + 4.5)
print(3 * (4 + 5))

print(10 % 3)

my_num = 5
print(my_num)

# Num to string
print(str(my_num) + "hey")

# Common math functions
# absolute value...
my_num = -5
print(abs(my_num))

# power >> hatvanyozas...
print(pow(3, 2))

print(max(4, 6))
print(min(4, 6))

print(round(3.2))
print(round(3.7))

# Importing math
from math import *

print(floor(5.7))
print(ceil(4.2))

# square root >> gyok
# google different math functions
print(sqrt(36))
