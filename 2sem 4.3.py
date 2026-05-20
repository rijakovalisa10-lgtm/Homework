import itertools


def shortest_superstring(words):
    best = None

    for p in itertools.permutations(words):
        curr = p[0]
        for i in range(1, len(p)):
            nxt = p[i]
            if nxt in curr:
                continue
            o = 0
            for j in range(min(len(curr), len(nxt)), 0, -1):
                if curr.endswith(nxt[:j]):
                    o = j
                    break
            curr += nxt[o:]

        if best is None or len(curr) < len(best):
            best = curr

    return best