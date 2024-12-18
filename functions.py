def is_palindrome(word):
    word = word.casefold()
    print(word, end=": ")
    return True if word[:] == word[::-1] else False


arsenal = is_palindrome("Arsenal")
print(arsenal)

anna = is_palindrome("Anna")
print(anna)

bob = is_palindrome("B.O.B")
print(bob)

majax = is_palindrome("Majax")
print(majax)
