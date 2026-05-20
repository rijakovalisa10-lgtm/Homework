def can_get_rich(n, exchanges):
    graph = [[] for _ in range(n)]

    for source, target, rate in exchanges:
        log_rate = -__import__('math').log(rate)
        graph[source].append((target, log_rate))

    dist = [float('inf')] * n
    dist[0] = 0

    for _ in range(n - 1):
        updated = False
        for u in range(n):
            if dist[u] != float('inf'):
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        updated = True
        if not updated:
            break

    for u in range(n):
        if dist[u] != float('inf'):
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    return True

    return False
