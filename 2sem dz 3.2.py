import sys
from collections import deque


class Node:
    def __init__(self):
        self.children = {}
        self.to = {}
        self.sufflink = None
        self.compressed_sufflink = None
        self.output = None


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def add(self, s):
        v = self.root
        for c in s:
            if c not in v.children:
                v.children[c] = Node()
            v = v.children[c]
        v.output = s

    def build(self, alphabet):
        queue = deque()
        self.root.sufflink = self.root
        self.root.compressed_sufflink = self.root

        for char in alphabet:
            if char in self.root.children:
                self.root.to[char] = self.root.children[char]
            else:
                self.root.to[char] = self.root

        for char in self.root.children:
            child = self.root.children[char]
            child.sufflink = self.root
            child.compressed_sufflink = self.root
            queue.append(child)

        while queue:
            u = queue.popleft()
            for char in alphabet:
                if char in u.children:
                    u.to[char] = u.children[char]
                else:
                    u.to[char] = u.sufflink.to.get(char, self.root)

            for char, v in u.children.items():
                v.sufflink = u.sufflink.to.get(char, self.root)
                if v.sufflink.output:
                    v.compressed_sufflink = v.sufflink
                else:
                    v.compressed_sufflink = v.sufflink.compressed_sufflink
                queue.append(v)


def solve():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    if not s or not t:
        return

    shifts = {s[i:] + s[:i] for i in range(len(s))}
    alphabet = sorted(list(set(s + t)))

    ac = AhoCorasick()
    for shift in shifts:
        ac.add(shift)
    ac.build(alphabet)

    ans = 0
    curr = ac.root
    for char in t:
        curr = curr.to.get(char, ac.root)
        temp = curr
        while temp and temp != ac.root:
            if temp.output:
                ans += 1
            temp = temp.compressed_sufflink

    print(ans)


if __name__ == "__main__":
    solve()