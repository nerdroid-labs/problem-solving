# Backtracking
### 문제해결 방식
+ 기본적으로 모든 경우의 수를 고려하는 알고리즘으로, 상태 공간을 트리로 나타낼 수 있을 때 적합한 방식이다.
+ 방식에 따라서, 깊이우선탐색(Depth First Search, DFS)과 너비우선탐색(Breadth First Search, BFS), 최선 우선 탐색(Best First Search/Heuristic Search) 등을 사용한다.
+ 탐색 과정에서 다음 노드를 선택할 때, **해가 될 수 있는 특정한 조건을 만족하는 경우에만**을 선택하는 방식으로 경우의 수를 줄인다.
+ 그리고 다음에 선택할 수 있는 노드 중, 어떠한 노드도 해가 될 수 있는 조건을 만족하지 못한다면 Parent 노드로 이동하여 다른 Child 노드를 선택하도록 한다.

### 관련하여 풀었던 문제
+ BOJ
  + [15649](https://www.acmicpc.net/problem/15649)
  + [15650](https://www.acmicpc.net/problem/15650)
  + [15651](https://www.acmicpc.net/problem/15651)
  + [15652](https://www.acmicpc.net/problem/15652)
  + [9663](https://www.acmicpc.net/problem/9663)
  + [2580](https://www.acmicpc.net/problem/2580)
  + [14888](https://www.acmicpc.net/problem/14888)
  + [14889](https://www.acmicpc.net/problem/14889)
