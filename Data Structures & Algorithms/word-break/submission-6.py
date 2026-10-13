# Trie + 1 DP approach

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
              node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.end_of_word = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Build Trie
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        # initialize the dp array
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            node = trie.root
            for j in range(i, n):
                if s[j] in node.children: # is the current character the child of the current node?
                    node = node.children[s[j]] # if yes, then traverse to the child
                    if node.end_of_word :
                        if dp[j+1] == True: # checking if the remaining suffix is segmentable or not.
                            dp[i] = True
                            break
                else :
                    break # if not, then stop traversing for that i
        
        return dp[0]
        