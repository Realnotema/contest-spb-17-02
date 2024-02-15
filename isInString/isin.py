def leng(s: str) -> int:
    uniq_symb = []
    answer = []
    for start in range(len(s)):
        now = start
        cnt = 0
        while now < len(s) and s[now] not in uniq_symb:
            uniq_symb.append(s[now])
            now += 1
            cnt += 1
        uniq_symb.clear()
        answer.append(cnt)
    return answer

file = open("tests/09")
fileout = open("tests/09.a", 'w')
s = file.readline()
fileout.write(str(max(leng(s))))