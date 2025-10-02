s = "amazing"
vowels = set("aeiou")
result = []

for ch in s:
    if ch not in vowels:
        result.append(ch)

print(result)
