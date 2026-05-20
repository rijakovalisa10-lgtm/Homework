def can_get_rich(exchanges, start):
    currencies = []
    for u, v, rate in exchanges:
        if u not in currencies:
            currencies.append(u)
        if v not in currencies:
            currencies.append(v)

    if start not in currencies:
        return False

    money = {}
    for c in currencies:
        money[c] = 0.0
    money[start] = 1.0

    for i in range(len(currencies) - 1):
        for u, v, rate in exchanges:
            if money[u] * rate > money[v]:
                money[v] = money[u] * rate

    for u, v, rate in exchanges:
        if money[u] * rate > money[v]:
            return True

    return False