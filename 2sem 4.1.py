class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def delete(self, word):
        def _del(node, w, d):
            if d == len(w):
                if '#' in node:
                    del node['#']
                return len(node) == 0
            c = w[d]
            if c not in node:
                return False
            if _del(node[c], w, d + 1):
                del node[c]
                return len(node) == 0
            return False

        _del(self.root, word, 0)