vowels_2 = set('aaeeiioouu')


word = input("Provide a word or a sentence to find vowels: ")

#vowel_found = {}
vowel_found = vowels_2.intersection(set(word))


for vowels_2 in vowel_found:
    print(vowels_2)

