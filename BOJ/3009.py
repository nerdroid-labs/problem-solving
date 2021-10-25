while True:
    line = input().strip()
    if line == "0 0 0":
        break

    a, b, c = map(int, line.split())
    a, b, c = sorted([a, b, c])

    a_length = a < b + c
    b_length = b < a + c
    c_length = c < a + b
    
    basic_cond = a_length and b_length and c_length
    square_cond = a ** 2 + b ** 2 == c ** 2

    if basic_cond and square_cond:
        print("right")
    else:
        print("wrong")