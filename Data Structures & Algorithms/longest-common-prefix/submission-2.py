# Optimized solution
class TrieNode:
    def __init__(self):
        self.children = {}

    def to_dict(self):
        return {
            ch: child.to_dict()
            for ch, child in self.children.items()
        }

    def __str__(self):
        return str(self.to_dict())

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = TrieNode()
        node = trie

        for word in strs:
            node = trie
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

        lcp = ""
        node = trie
        while True:
            if len(node.children.keys()) == 1:
                key = list(node.children.keys())[0]
                lcp += key
                node = node.children[key]
            else:
                return lcp

        
        # print (trie)
        


                    
                            