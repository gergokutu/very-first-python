## Functions
# collection of code
# which performs a specific task

def say_hi():
  # next line has to be intended
  print("Hello User")

print("- before -")
# call it
say_hi() 
print("- after -")

# parameters >> e.g. name, age
def say_hello(name, age):
  print("What's up " + name + "?\nYou are under " + str(age) + "? Huhh?\n\n")

say_hello("Pista", 21)

name = "Lulu"
age = 18
say_hello(name, age)
say_hello("Bözske", 45)
