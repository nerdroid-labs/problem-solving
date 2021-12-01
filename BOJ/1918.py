import sys
import collections
def input(): return sys.stdin.readline().strip()


line = input()
low_op = ["+", "-"]
high_op = ["*", "/"]
parenthesis = ["(", ")"]
priority = {"-": 0, "+": 0, "/": 1, "*":1}


def toPostfix(exp):
    operator = collections.deque()
    operand = collections.deque()
    parenthesis_exp = ""
    parenthesis_ctr = 0

    for c in exp:
        update = False

        if c in parenthesis or parenthesis_ctr > 0:
            if c == "(": parenthesis_ctr += 1
            elif c == ")": parenthesis_ctr -= 1
            parenthesis_exp += c

            if parenthesis_ctr == 0:
                parenthesis_exp = parenthesis_exp[1:-1]
                operand.append(toPostfix(parenthesis_exp))
                parenthesis_exp = ""
                update = len(operator) > 1

        elif c in priority.keys():
            operator.append(c)

        else:
            operand.append(c)
            update = len(operator) > 1

        if update and priority[operator[-1]] > priority[operator[-2]]:
            sub_answer = ""
            for i in range(2):
                sub_answer = operand.pop() + sub_answer
            sub_answer += operator.pop()
            operand.append(sub_answer)

    while operator:
        sub_answer = ""
        for i in range(2): sub_answer += operand.popleft()
        sub_answer += operator.popleft()
        operand.appendleft(sub_answer)

    return operand[0].strip()


print(toPostfix(line))
