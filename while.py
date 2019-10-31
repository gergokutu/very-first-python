## while loop
# bare basics...
i = 1
while i <= 10:
  print(i)
  # i = i + 1
  i += 1

print("Done with loop")

## Guessing Game >> password
password = "shark"
guess = ""

while guess != password:
  guess = input("Enter the password: ")

print("Correct!")