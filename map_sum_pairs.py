class TrieNode():
    def __init__(self, count = 0):
        self.count = count
        self.children = {}

class MapSum():
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        # time: O(k)
        curr = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        curr.count+=delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count+=delta

    def sum(self, prefix):
        # time: O(k)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count 

