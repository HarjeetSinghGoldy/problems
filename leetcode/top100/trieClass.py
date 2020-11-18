class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}

    # def insert(self, word: str) -> None:
    #     """
    #     Inserts a word into the trie.
    #     """
    #     self.hashMap[word] = 1
    def insert(self, word):
        t = self.hashMap
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    # def search(self, word: str) -> bool:
    #     """
    #     Returns if the word is in the trie.
    #     """
    #     if word in self.hashMap:
    #         return True
    #     else:
    #         return False
    def search(self, word):
        t = self.hashMap
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    # def startsWith(self, prefix: str) -> bool:
    #     """
    #     Returns if there is any word in the trie that starts with the given prefix.
    #     """
    #     words = self.hashMap.keys()
    #     for i,word in enumerate(words):
    #         if prefix in word:
    #             return True
    #     return False
    def startsWith(self, prefix):
        t = self.hashMap
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_2 = obj.search("app")
param_3 = obj.startsWith("app")
obj.insert("harjeet")
param_4 = obj.search("harjeet")

obj.insert("app")

print(obj)
