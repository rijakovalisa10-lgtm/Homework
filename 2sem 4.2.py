def count_cyclic_shifts(text, s):
    n = len(s)
    shifts = set()

    for i in range(n):
        shifts.add(s[i:] + s[:i])

    total_count = 0
    for shift in shifts:
        pos = text.find(shift)
        while pos != -1:
            total_count += 1
            pos = text.find(shift, pos + 1)

    return total_count