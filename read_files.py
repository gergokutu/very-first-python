## Reading from external files

# open("file", "mode")
# "r" >> read
# "w" >> write
# "r+" >> read & write
# "a" >> append (info to the end of the file)
employee_file = open("employees.txt", "r")

# Check readability
print(employee_file.readable()) # returns a boolean

# Read the file
# literally grab out the content
# that's why other read options gives back empty things below
# if the next line is not commented out
# print(employee_file.read())

# Read just a single line of the file
# starts with the first (0 index by default)
# you can repeat it
print(employee_file.readline())
print(employee_file.readline())

# Read (literally!) multiple lines and put them into an array
print(employee_file.readlines())

# You have to close it, too!!!
employee_file.close()

##################################
employee_file2 = open("employees.txt", "r")

# access to specific line
print(employee_file2.readlines()[0])
employee_file2.close()

##################################
# print out all the employees from the file with for loop
employee_file3 = open("employees.txt", "r")
for employee in employee_file3.readlines():
  print(employee)

employee_file3.close()