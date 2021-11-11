def search_for_vowels(phrase:str) -> set:
    """Return any vowels found in a word or sentence."""
    vowel = set('aeiou')
    return vowel.intersection(set(phrase))

# search_for_vowels(word)
# word = input("Please input a word or sentence: ")

def search_for_letters(phrase:str, letters:str ='aeiou') -> set:
    """Return a set of letters found in phrase"""
    return set(letters).intersection(set(phrase))

