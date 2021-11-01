ret = []
for i in range(int(input())):
    num = int(input())

    if num == 0:
        ret.pop()
    else:
        ret.append(num)

print(sum(ret))