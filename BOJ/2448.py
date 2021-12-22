def make(n):
	if n == 3:
		return [
			"  *  ",
			" * * ",
			"*****"
		]
	else:
		substar = make(n // 2)

		made = []
		shift = n // 2
		for line in substar:
			made.append(shift * " " + line + shift * " ")

		for line in substar:
			made.append(line + " " + line)

		return made


N = int(input())
print(*make(N), sep="\n")
