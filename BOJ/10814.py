N = int(input())

members = []
for i in range(N):
    member = input().split()
    member[0] = int(member[0])
    member.append(i)
    members.append(member)

members.sort(key=lambda x: (x[0], x[2]))

for age, name, _ in members:
    print(age, name)