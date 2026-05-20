def find_eulerian_path(n, edges):
    if not edges:
        return True, []


graph = [[] for _ in range(n)]
degree = [0] * n

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
    degree[u] += 1
    degree[v] += 1

odd_vertices = []
for i in range(n):
    if degree[i] % 2 == 1:
        odd_vertices.append(i)

if len(odd_vertices) > 2:
    return False, []

start = 0
if odd_vertices:
    start = odd_vertices[0]

path = []
stack = [start]
used = set()

while stack:
    u = stack[-1]
    found = False

    for v in graph[u]:
        edge = tuple(sorted((u, v)))
        if edge not in used:
            used.add(edge)
            stack.append(v)
            found = True
            break

    if not found:
        path.append(stack.pop())

path.reverse()

if len(path) - 1 != len(edges):
    return False, []

return True, path
