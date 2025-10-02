first = "first"
third = "third"

common = []

for letter in first:
    if letter in third and letter not in common:
        common.append(letter)

print(common)
