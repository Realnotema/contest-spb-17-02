def isPalindrome(string) -> bool:
    if string == string[::-1]:
        print("ret true")
        return True
    else:
        return False

file = open('tests/98', 'r')
a = file.readlines()
print(a)
print(isPalindrome(a))