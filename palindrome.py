def is_palindrome(word):
    plain = "".join(e for e in word if e.isalnum()).lower()
    new_word = plain[::-1]
    return True if new_word == plain else False
    
print(is_palindrome("Step on no pets"))
