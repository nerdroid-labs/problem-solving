input()
string = input()

r, M, offset = 31, 1234567891, 96
ret = 0
for i in range(len(string)):
    ret += (r ** i) * (ord(string[i]) - offset)

print(ret % M)
