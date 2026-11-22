# Trie Approach

# Messy Code
# Optimized solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

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
            node.end_of_word = True
            
        lcp = ""
        node = trie
        while True:
            if len(node.children) == 1 and node.end_of_word == False:
                key = list(node.children.keys())[0]
                lcp += key
                node = node.children[key]
            else:
                return lcp
                
                
# Clean Code 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        trie = self.root
        node = trie

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end_of_word = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.insert(word)
            
        lcp = []
        node = trie.root
        while True:
            if len(node.children) == 1 and node.end_of_word == False:
                key = list(node.children.keys())[0]
                lcp.append(key)
                node = node.children[key]
            else:
                return "".join(lcp)

        
        


                    
                            
