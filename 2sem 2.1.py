def solve(n, queries):
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

    return ans[::-1]