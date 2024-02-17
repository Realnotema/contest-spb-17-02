def roman_to_int(s):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and val[s[i]] > val[s[i - 1]]:
            result += val[s[i]] - 2 * val[s[i - 1]]
        else:
            result += val[s[i]]
    return result

s = str(input())
print(roman_to_int(s))