import sys

sys.setrecursionlimit(200000)


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    idx = 3 + 2 * m

    queries = []
    for _ in range(k):
        op = data[idx]
        u = int(data[idx + 1])
        v = int(data[idx + 2])
        queries.append((op, u, v))
        idx += 3

    p = list(range(n + 1))

    def get(x):
        if p[x] != x:
            p[x] = get(p[x])
        return p[x]

    ans = []
    for op, u, v in queries[::-1]:
        if op == 'cut':
            p[get(u)] = get(v)
        else:
            if get(u) == get(v):
                ans.append('YES')
            else:
                ans.append('NO')

    for res in ans[::-1]:
        print(res)


if __name__ == '__main__':
    main()