def min_edge_cover(n, m, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    matching = [-1] * (m + 1)
    used = [False] * (n + 1)

    def kuhn(u):
        if used[u]:
            return False
        used[u] = True
        for v in adj[u]:
            if matching[v] == -1 or kuhn(matching[v]):
                matching[v] = u
                return True
        return False

    for i in range(1, n + 1):
        used = [False] * (n + 1)
        kuhn(i)

    cover = []
    covered_left = [False] * (n + 1)
    covered_right = [False] * (m + 1)

    for v in range(1, m + 1):
        if matching[v] != -1:
            u = matching[v]
            cover.append((u, v))
            covered_left[u] = True
            covered_right[v] = True

    for u in range(1, n + 1):
        if not covered_left[u] and adj[u]:
            v = adj[u][0]
            cover.append((u, v))
            covered_right[v] = True

    rev_adj = [[] for _ in range(m + 1)]
    for u, v in edges:
        rev_adj[v].append(u)

    for v in range(1, m + 1):
        if not covered_right[v] and rev_adj[v]:
            u = rev_adj[v][0]
            cover.append((u, v))

    return cover