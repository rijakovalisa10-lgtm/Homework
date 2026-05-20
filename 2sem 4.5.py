def match_with_wildcards(text, pattern):
    n = len(text)
    m = len(pattern)
    res = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if pattern[j] != '?' and pattern[j] != text[i + j]:
                match = False
                break
        if match:
            res.append(i)

    return res