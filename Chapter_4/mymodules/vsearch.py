def search_for_vowels(phrase: str) -> set:
    """Return any vowels found in a word or sentence."""
    vowel = set('aeiou')
    return vowel.intersection(set(l.lower() for l in phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of letters found in phrase"""
    # phrase = phrase.lower()
    return set(letters).intersection(set(l.lower() for l in phrase))
