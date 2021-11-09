vowels = ['a','e','i','o','u']

word = input("Provide a word or a sentence to find vowels: ")
vowel_found = []

for letter in word:
    if letter in vowels:
        if letter not in vowel_found:
            vowel_found.append(letter)
for vowel in vowel_found:
    print(vowel)