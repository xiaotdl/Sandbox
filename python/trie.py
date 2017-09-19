# == iterative implementation ==
# class TrieNode:
#     def __init__(self, char):
#         self.char = char
#         self.next = [None for x in range(26)]
#         self.hasWord = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode(' ')

#     def insert(self, word):
#         curr = self.root
#         for char in word:
#             i = ord(char) - ord('a')
#             if curr.next[i] == None:
#                 curr.next[i] = TrieNode(char)
#             curr = curr.next[i]
#         curr.hasWord = True

#     def search(self, word):
#         node = self.searchPrefix(word)
#         return node != None and node.hasWord

#     def startsWith(self, prefix):
#         node = self.searchPrefix(prefix)
#         return node != None

#     def searchPrefix(self, prefix):
#         curr = self.root
#         for char in prefix:
#             i = ord(char) - ord('a')
#             if curr.next[i] == None:
#                 return None
#             curr = curr.next[i]
#         return curr

# == recursive implementation ==
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.next = [None for x in range(26)]
        self.hasWord = False

    def insert(self, word, pos):
        if (pos == len(word)):
            self.hasWord = True
            return

        c = word[pos]
        i = ord(c) - ord('a')
        if (self.next[i] == None):
            self.next[i] = TrieNode(c)
        self.insert(word, pos + 1)

    def search(self, word, pos):
        if (pos == len(word)):
            return self

        c = word[pos]
        i = ord(c) - ord('a')
        if (self.next[i] == None):
            return None
        return self.search(word, pos + 1)

class Trie:
    def __init__(self):
        self.root = TrieNode(' ')

    def insert(self, word):
        self.root.insert(word, 0)

    def search(self, word):
        node = self.root.search(word, 0)
        return node != None and node.hasWord

    def startsWith(self, prefix):
        node = self.root.search(prefix, 0)
        return node != None

trie = Trie()
trie.insert("leetcode")
print trie.search("leetcode")
print trie.startsWith("leet")
