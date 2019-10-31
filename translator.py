# Pocok language
# vowels >> p
# --------------
# dog >> dpg
# cat >> cpt

def translate(phrase):
  translation = ""
  for letter in phrase:
    # check if the letter is a vowel
    if letter in "AEIOUaeiou":
      translation = translation + "p"
    else:
      translation = translation + letter
  return translation

print(translate(input("Enter a phrase for translate func: ")))

def translate2(phrase):
  translation = []
  for letter in phrase:
    # check if the letter is a vowel
    if letter.lower() in "aeiou":
      # keep the uppercase
      if letter.isupper():
        translation.append("P")
      else:
        translation.append("p")

    else:
      translation.append(letter)
  return translation

print(translate2(input("Enter a phrase for translate2 func: ")))