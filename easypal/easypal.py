def isPalindrome(string) -> bool:
    if string == string[::-1]:
        print("ret true")
        return True
    else:
        return False