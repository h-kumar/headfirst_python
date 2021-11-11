import vsearch

def test_vsearch():
    test_1 = vsearch.search_for_vowels("Hello")
    test_2 = vsearch.search_for_letters("Hello","aeiou")
    print(test_1)
    print(test_2)


if __name__ == "__main__":
    test_vsearch()