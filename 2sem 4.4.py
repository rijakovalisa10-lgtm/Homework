def count_prefixes(s):
    n = len(s)
    pi = [0] * n

    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    ans = [1] * n
    for i in range(n - 1, 0, -1):
        if pi[i] > 0:
            ans[pi[i] - 1] += ans[i]

    return ans