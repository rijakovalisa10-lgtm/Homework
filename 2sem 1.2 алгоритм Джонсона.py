import heapq


def johnson(vertices, edges):
    edges_q = list(edges)
    for v in vertices:
        edges_q.append(('q', v, 0))

    h = {}
    for v in vertices + ['q']:
        h[v] = float('inf')
    h['q'] = 0

    for i in range(len(vertices)):
        for u, v, w in edges_q:
            if h[u] + w < h[v]:
                h[v] = h[u] + w

    for u, v, w in edges_q:
        if h[u] + w < h[v]:
            return None

    graph = {}
    for v in vertices:
        graph[v] = []

    for u, v, w in edges:
        new_w = w + h[u] - h[v]
        graph[u].append((v, new_w))

    res = {}
    for start in vertices:
        dist = {}
        for v in vertices:
            dist[v] = float('inf')
        dist[start] = 0

        pq = [(0, start)]

        while len(pq) > 0:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        res[start] = {}
        for v in vertices:
            if dist[v] != float('inf'):
                res[start][v] = dist[v] + h[v] - h[start]
            else:
                res[start][v] = float('inf')

    return res