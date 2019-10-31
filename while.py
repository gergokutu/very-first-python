## while loop
# bare basics...
i = 1
while i <= 10:
  print(i)
  # i = i + 1
  i += 1

print("Done with loop")

## Guessing Game >> password
# 3 tries
password = "shark"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != password and not(out_of_guesses):
  if guess_count < guess_limit:
    guess = input("Enter the password: ")
    guess_count += 1
  else:
    out_of_guesses = True

if out_of_guesses:
  print("Out of guesses, YOU LOSE!")
else:
  print("Correct!")