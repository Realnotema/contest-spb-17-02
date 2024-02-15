def isAnag(str1, str2) -> bool: 
    if(sorted(str1)== sorted(str2)): 
        return True 
    else: 
        return False 
        
string1 = str(input())
string2 = str(input())
print(isAnag(string1, string2))