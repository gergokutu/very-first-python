## Dictionaries >> key-value pairs (objects)
# convert 3 digit month name into full month name!
# pretty good use case for dictionary
monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "Apil",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "Augustus",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December",
}

# access
print(monthConversions["Nov"])
# key error
# print(monthConversions["PPP"])
print(monthConversions.get("March")) # defines default value
print(monthConversions.get("AMS", "Not a valid key"))
