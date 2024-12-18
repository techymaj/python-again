def is_palindrome(word):
    """
    Checks whether the word is a palindrome.
    :param word: The word to check.
    :return: A friendly message: `str`, that confirms whether word is a palindrome or not.
    """
    word = word.casefold()
    return f"{word} is a palindrome" if word == word[::-1] else f"{word} is not a palindrome"


while True:
    word_to_check = input("Enter a word to check: (Qq to quit) ")
    if word_to_check == "Q".casefold():
        break
    check_palindromeness = is_palindrome(word_to_check)
    print(check_palindromeness)
