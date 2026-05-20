import sys
from collections import deque


def edmonds_karp(graph, source, sink, n):
    flow = 0
    parent = [-1] * (n + 1)

    while True:
        for i in range(n + 1):
            parent[i] = -1
        parent[source] = source
        q = deque([source])

        while q:
            u = q.popleft()
            for v in range(1, n + 1):
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

    return flow