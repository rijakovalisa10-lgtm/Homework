class Node:
    def __init__(self):
        self.children = {}
        self.output = None


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s):
        v = self.root
        for c in s:
            if c not in v.children:
                v.children[c] = Node()
            v = v.children[c]
        v.output = s

    def search(self, s):
        v = self.root
        for c in s:
            if c not in v.children:
                return False
            v = v.children[c]
        return v.output is not None

    def delete(self, s):
        def _remove(v, s, i):
            if i == len(s):
                if v.output is None:
                    return False
                v.output = None
                return len(v.children) == 0

            c = s[i]
            if c not in v.children:
                return False

            if _remove(v.children[c], s, i + 1):
                del v.children[c]
                return v.output is None and len(v.children) == 0
            return False

        _remove(self.root, s, 0)