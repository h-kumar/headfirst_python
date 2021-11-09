vowels = ['a','e','i','o','u']

word = input("Provide a word or a sentence to find vowels: ")

vowel_found = {}

for letter in word:
    if letter in vowels:
        vowel_found.setdefault(letter,0)
        vowel_found[letter] += 1
for k,v in sorted(vowel_found.items()):
    print(k, 'was found',v, 'time(s).' )

