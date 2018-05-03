class WordDictionary():
    def __init__(self):
        self.word_dict = {}

    def addWord(self, word):
        if word:
            self.word_dict.get(len(word), []).append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict.get(len(word))
        for v in self.word_dict.get(len(word)):
            for i, ch in enumerate(word):
                if ch!=v[i] and ch!='.':
                    break
            else:
                return True
        return False




class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word):
        return self.searchFrom(self.root, word)

    def searchFrom(self, node, word):
        for i in xrange(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word