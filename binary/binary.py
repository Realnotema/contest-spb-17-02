def fu():
    string = str(input())
    if string.isdigit() != True:
        print("ERROR")
    else:
        print(len(string) - string.count('0'))

fu()