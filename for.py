## For loops
# loop over different collection of items (e.g. arrays)
# print out each letter of Giraffe Academy
for letter in "Giraffe Academy":
  print(letter)

friends = ["Jimbo", "Pista", "Józsi", "Gizi"]
for friend in friends:
  print(friend)

for index in range(3, 10):
  print(index)

# another way to print out all the elements in an array
for index in range(len(friends)):
  print(friends[index])

for index in range(5):
  if index == 0:
    print("First iteration")
  elif index == 4:
    print("Last iteration")
  else:
    print("Index is: " + str(index))
  
## exponent function with for loop
# same as e.g. print(2**3)
def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result
  
print(raise_to_power(3, 2))