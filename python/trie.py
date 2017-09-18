class TrieNode:
    def __init__(self, char):
        self.char = char
        self.next = [None for x in range(26)]
        self.hasWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode(' ')

    def insert(self, word):
        curr = self.root
        for char in word:
            i = ord(char) - ord('a')
            if curr.next[i] == None:
                curr.next[i] = TrieNode(char)
            curr = curr.next[i]
        curr.hasWord = True

    def search(self, word):
        node = self.searchPrefix(word)
        return node != None and node.hasWord

    def startsWith(self, prefix):
        node = self.searchPrefix(prefix)
        return node != None

    def searchPrefix(self, prefix):
        curr = self.root
        for char in prefix:
            i = ord(char) - ord('a')
            if curr.next[i] == None:
                return None
            curr = curr.next[i]
        return curr

trie = Trie()
trie.insert("leetcode")
print trie.search("leetcode")
print trie.startsWith("leet")
