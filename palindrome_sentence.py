def palindrome_sentence(sentence):
    lower_cased = sentence.casefold()
    splits = lower_cased.split()
    new_sentence = "".join(splits)
    print(f"After splitting and joining: {new_sentence}")
    if new_sentence.isalnum():
        return palindrome_or_not(checked=new_sentence, entered_word=sentence)
    else:
        has_non_alnum_chars = "".join((
            c for c in new_sentence if c.isalnum() is True
        ))
        print("Alphanumeric characters detected:")
        print(f"After removing alphanumeric characters: {has_non_alnum_chars}")
        return palindrome_or_not(checked=has_non_alnum_chars, entered_word=sentence)


def palindrome_or_not(checked="", entered_word="entered_word"):
    if checked == checked[::-1]:
        return f"{entered_word} is a palindrome"
    else:
        return f"{entered_word} is not a palindrome"


while True:
    sentence_to_check = input("Type a sentence to check: (Qq) to quit: ")
    if sentence_to_check == "Q".casefold():
        break
    palindromeness = palindrome_sentence(sentence_to_check)
    print(palindromeness)
