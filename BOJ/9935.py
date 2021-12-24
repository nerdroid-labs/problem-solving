import sys


def input():
	return sys.stdin.readline().rstrip()


text = input()
bomb = input()
stack = []

for i in range(len(text)):
	stack.append(text[i])

	if len(stack) >= len(bomb):
		substring = "".join(stack[-len(bomb):])

		if substring == bomb:
			for _ in range(len(bomb)):
				stack.pop()

text = "".join(stack)

if not text:
	print("FRULA")
else:
	print(text)
