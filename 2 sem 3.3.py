import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    b = [int(x) for x in data[n+1:2*n+1]]
    m = int(data[2*n+1])

    total_vertices = 2 * n + 2
    source = 0
    sink = total_vertices - 1

    graph = [[0] * total_vertices for _ in range(total_vertices)]

    for j in range(n):
        graph[source][j + 1] = b[j]

    for i in range(n):
        graph[n + 1 + i][sink] = a[i]

    idx = 2 * n + 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        graph[v][n + u] = float('inf')
        idx += 2

    flow = 0
    parent = [-1] * total_vertices

    while True:
        for i in range(total_vertices):
            parent[i] = -1
        parent[source] = source
        q = deque([source])

        while q:
            u = q.popleft()
            for v in range(total_vertices):
                if parent[v] == -1 and graph[u][v] > 0:
                    parent[v] = u
                    q.append(v)

        if parent[sink] == -1:
            break

        path_flow = float('inf')
        curr = sink
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, graph[prev][curr])
            curr = prev

        curr = sink
        while curr != source:
            prev = parent[curr]
            graph[prev][curr] -= path_flow
            graph[curr][prev] += path_flow
            curr = prev

        flow += path_flow

    if flow == sum(a):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()