import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current is None:
                return False
        return current.is_end

    def startWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current is None:
                return False
        return True


words = ["dog", "cat", "apple", "apricot", "fish"]
trie = Trie()
for word in words:
    trie.insert(word)

unique_prefixes = [trie.startWith(word) for word in words]
print(unique_prefixes)