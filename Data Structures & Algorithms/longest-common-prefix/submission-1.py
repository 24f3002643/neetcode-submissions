# Optimized solution
class TrieNode:
    def __init__(self):
        self.children = {}

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
        
        print (trie)
        


                    
                            