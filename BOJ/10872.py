N = int(input())

numbers = [1]
for i in range(N): numbers.append(i+1)

fact = 1
while numbers:
   fact *= numbers.pop()

print(fact)