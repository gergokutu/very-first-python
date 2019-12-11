## List functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Tom"]
print(friends)

friends.append("YAAAAEEEL")
print(friends)

# takes two parameters (index, "word_to_insert")
friends.insert(1, "Kelly")
print(friends)

friends.remove("YAAAAEEEL")
print(friends)

print(friends.index("Kevin"))
print(friends.count("Jim"))

friends.sort()
print(friends)

lucky_numbers.sort(reverse = True)
print(lucky_numbers)

friends2 = friends.copy()
friends2.extend(lucky_numbers)
print(friends2)

