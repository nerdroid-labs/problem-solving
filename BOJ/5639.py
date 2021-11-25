import sys
sys.setrecursionlimit(10 ** 5)

root = None
def add_node(add_value):
    global root

    if root is None: root = [add_value, None, None]
    else:
        current_node = root
        while True:
            value, left, right = current_node

            if value > add_value:
                if left is None:
                    current_node[1] = [add_value, None, None]
                    break
                else: current_node = left

            elif value < add_value:
                if right is None:
                    current_node[2] = [add_value, None, None]
                    break
                else: current_node = right


def post_order(node):
    if node is None: return

    value, left, right = node
    post_order(left)
    post_order(right)
    print(value)


for line in sys.stdin:
    add_node(int(line))

post_order(root)
