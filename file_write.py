## Write and append files
# append (add to the end)
# animal_file = open("animals.txt", "a")
# animal_file.write("\nEeyore - Donkey")
# animal_file.close()

# write a file » overwrite the entire file
# only Eeyore gonna be in the animals.txt file
# animal_file = open("animals.txt", "w")
# animal_file.write("Eeyore - Donkey")
# animal_file.close()

# create a new file >> animals2.txt
# animal_file = open("animals2.txt", "w")
# animal_file.write("Eeyore - Donkey")
# animal_file.close()

# write an webpage (html file) inside python
webpage = open("index.html", "w")
webpage.write("<DOCTYPE! html>")
webpage.write("\n<html>")
webpage.write("\n<title>---Python---</title>")
webpage.write("\n</head>")
webpage.write("\n<body>")
webpage.write("\n<h1>Html file written by Python</h1>")
webpage.write("\n</body>")
webpage.write("\n</html>")
webpage.close()