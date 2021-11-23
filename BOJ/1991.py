import sys
import collections
def input(): return sys.stdin.readline().rstrip()

N = int(input())
graph = dict()

for _ in range(N):
    node, left, right = input().split()
    graph[node] = [left, right]

def preorder(node):
    print(node, end="")
    left, right = graph[node]

    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

def inorder(node):
    left, right = graph[node]

    if left != '.':
        inorder(left)

    print(node, end="")

    if right != '.':
        inorder(right)

def postorder(node):
    left, right = graph[node]

    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)

    print(node, end="")


preorder('A')
print()

inorder('A')
print()

postorder('A')
print()
