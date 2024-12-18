def is_palindrome(word):
    word = word.casefold()
    return f"{word} is a palindrome" if word == word[::-1] else f"{word} is not a palindrome"


while True:
    word_to_check = input("Enter a word to check: (Qq to quit) ")
    if word_to_check == "Q".casefold():
        break
    check_palindromeness = is_palindrome(word_to_check)
    print(check_palindromeness)