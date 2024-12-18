def palindrome_sentence(sentence):
    lower_cased = sentence.casefold()
    splits = lower_cased.split()
    new_sentence = "".join(splits)
    print(f"After splitting and joining: {new_sentence}")
    if new_sentence.isalnum():
        return f"{sentence} is a palindrome" if new_sentence == new_sentence[::-1] else f"{sentence} is not a palindrome"
    else:
        sentence_with_non_alnum_characters = "".join((
            c for c in new_sentence if c.isalnum() is True
        ))
        print("Alphanumeric characters detected:")
        print(f"Removing alphanumeric character: {sentence_with_non_alnum_characters}")
        return f"{sentence} is a palindrome" if sentence_with_non_alnum_characters == sentence_with_non_alnum_characters[::-1] else f"{sentence} is not a palindrome"


while True:
    sentence_to_check = input("Type a sentence to check: (Qq) to quit: ")
    if sentence_to_check == "Q".casefold():
        break
    palindromeness = palindrome_sentence(sentence_to_check)
    print(palindromeness)
