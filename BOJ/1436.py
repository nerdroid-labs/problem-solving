N = int(input())

found = 0
num = 0

while found < N:
    num += 1
    num_str = str(num)

    for i in range(3, len(num_str) + 1):
        if "6"*i in num_str:
            found += 1
            break

print(num)