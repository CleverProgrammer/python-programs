def is_palindrome(s):
    s = input("wrie: ")
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False 
    return is_palindrome(s[1:-1])
