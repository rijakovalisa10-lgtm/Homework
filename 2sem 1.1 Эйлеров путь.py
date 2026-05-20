def eulerian_path(edges):
    graph = {}
    in_deg = {}
    out_deg = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if u not in in_deg:
            in_deg[u] = 0
        if u not in out_deg:
            out_deg[u] = 0

        if v not in graph:
            graph[v] = []
        if v not in in_deg:
            in_deg[v] = 0
        if v not in out_deg:
            out_deg[v] = 0

        graph[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1

    start = None
    for node in graph:
        if out_deg[node] - in_deg[node] == 1:
            start = node

    if start is None and len(edges) > 0:
        start = edges[0][0]

    stack = [start]
    path = []

    while len(stack) > 0:
        curr = stack[-1]
        if len(graph[curr]) > 0:
            next_node = graph[curr].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())

    path.reverse()
    return path