def guess():
    a = str(input())
    if a.isdigit() != True:
        print("ERROR")
        return 0
    b = str(input())
    if b.isdigit() != True:
        print("ERROR")
        return 0
    else:
        print(1)
        return 0
    
guess()