def is_palindrome(word):
    word = word.lower()
    og_word = 0
    palindrome_word = len(word) -1
    while og_word < palindrome_word:
        if word[og_word] != word[palindrome_word]:
            return(False)
        og_word += 1
        palindrome_word -= 1
        return True

print(is_palindrome("racecar"))
print(is_palindrome("saw"))