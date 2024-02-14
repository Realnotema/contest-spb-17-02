import random
import string

def genpal():
    length = random.randint(3, 10**4)
    isNum = random.randint(0, 1)
    if isNum == 0:
        answer = ''.join(random.choice(string.ascii_lowercase) for i in range(length // 2))
    else:
        answer = ''.join(random.choice(string.digits) for i in range(length // 2))
    answer = answer + answer[::-1]
    if isNum == 1:
        isMin = random.randint(0, 1)
        if isMin == 1:
            print(False)
            answer = '-' + answer
            return answer
        else:
            print(True)
            return answer
    else:
        return answer

def gennum(filename):
    ans_filename = filename + '.a'
    ans_file = open(ans_filename, 'w')
    isPal = random.randint(0, 10)
    if isPal < 7:
        ans = genpal()
        if ans[0] == '-':
            ans_file.write("False")
        else: 
            ans_file.write("True")
        return ans
    else: 
        ans_file.write("False")
        print("False")
        length = random.randint(3, 10**4)
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

filename = '00'
for i in range(100):
    file = open(filename, 'w')
    file.write(gennum(filename))
    filename = str(int(filename) + 1)
    if int(filename) < 10:
        filename = '0' + filename