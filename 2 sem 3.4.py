import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    p_count = int(data[2])

    unsafe = set()
    idx = 3
    for _ in range(p_count):
        unsafe.add(int(data[idx]))
        idx += 1

    safe_edges = []
    hacker_edges = {}

    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        idx += 3

        u_bad = u in unsafe
        v_bad = v in unsafe

        if u_bad and v_bad:
            continue
        elif not u_bad and not v_bad:
            safe_edges.append((w, u, v))
        else:
            hacker = u if u_bad else v
            if hacker not in hacker_edges or w < hacker_edges[hacker]:
                hacker_edges[hacker] = w

    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False

    safe_edges.sort()
    total_cost = 0
    components = n - p_count

    for w, u, v in safe_edges:
        if union(u, v):
            total_cost += w
            components -= 1

    if n > p_count and components > 1:
        print("-1")
        return

    for h in unsafe:
        if h not in hacker_edges:
            print("-1")
            return
        total_cost += hacker_edges[h]

    print(total_cost)


if __name__ == '__main__':
    main()