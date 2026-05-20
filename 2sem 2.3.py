import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        graph[u].append(v)
        in_degree[v] += 1
        idx += 2

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    visited = 0
    unique = True

    while len(q) > 0:
        if len(q) > 1:
            unique = False

        u = q.popleft()
        visited += 1

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if visited < n:
        print("-1")
    elif unique:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()