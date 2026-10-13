## Trie
- First lets understand, What is Trie ? 
    - Trie is a tree, built of all the words of wordDict. [Note : Trie is a tree, built of `wordDict`, and not of the given string.]
    - In trie, each node (except the root node) represents a character and path from the root represents prefixes of words.
    - A branch in the tree diverge, when the two words stop having the same prefixes.
    - A full complete path from root represents a word in wordDict.
    - Also :
        - Trie need not be a binary tree.
        - The root node can have 1 child node, 2 child nodes or more than 2 child nodes. This is true for all other non-root nodes too.
        - A root can have maximum of 26 nodes, for each english alphabet letters (assuming that only either lower/upper case letters are allowed).    
    - We build one Trie and reuse it while processing every starting index i.


- What does each node in a trie contain? 
- Conceptually, each node contains :
    1. Children : links to the next character nodes.
    2. End-of-words-flag : Indicates whether a word ends at this node.     



## The idea in this approach 
- We start at a index i in s.
- We look for the child of root node having the character s[i].
- If it exists, we choose that path. Now we look for that child of this current node having the character s[i+1]. If it exists, we choose that node (or alternatively we can say that we traverse that path). 
- We continue doing so, till we reach the end of the string s.
- If at any point, the child of the current node is not same as the character at next index of s, we stop that search for that starting index i.
- If we reached till the end of the string s, it means that the substring starting at index i (s[i:]) exist in the wordDict.
- Suppose while traversing the branch of tree, the charcater in s at index k+1, does not match. Then we know that the substring s[i:k+1] exist in wordDict. Now we need to check whether the remaining substring s[k+1:] is segmentable or not. If the remaining substring is segmentable, then the string s[i:] is segmentable. For this, we need to check dp[k+1].
    - if dp[k+1] == True, this means that the substring s[k+1:] is segmentable.
    - if dp[k+1] == False, this means that the substring s[k+1:] is not segmentable.

`The above approach is wrong/ not fully correct.` 
- There are two separate checks : `end-of-word flag` checks and checking `whether a matching child exists for s[k]`.
- Point 6 : Reaching the end of `s` does not necessarily mean a dictionary word was found. The trie may contain a path matching all of s[i:], but the final node might not have its end-of-word flag set to True. The end-of-word flag determines whether a matched substring is a complete binary word.
- Point 7 : A mismatch does not prove that the preceding substring is a dictionary word. The mismatch only tells that we cannot extend the current match along that path. Whether the preceding substring is a complete word depends on the end-of-word flag at the current trie node

## Corrections in the Approach

1. Checking the `end-of-word` flag whenever a node is reached.
    - If `True`, `s[i:k]` is in wordDict. Now check `dp[k]` for remaining substring.
    - If `dp[k] == True`, set `dp[i] = True` and stop. We have found a valid segmentation.
    - If  `dp[k] == False`, keep traversing if the next character matches a Trie child. A longer word might work.
2. Check whether a matching child exists for `s[k]`.
    - If it exists, follow that child and continue.
    - If it doesn't, stop traversal for this starting index. No longer word matching the input can be found along this path.

So what we do : 
- We traverse the tree along a branch (checking whether a matching child exists for s[k]).
- At every node that we reach, check its end-of-word flag. 
    - If it is `True`, check whether the remaining suffix is segmentable using dp or not.
    - If it is `False`, and a matching child  exists for the next character, continue traversing. If no matching child exists, stop.

## Now how to apply this approach
- so to check whether the string s is fully segementable or not. So we need to start from index 0.
- we need to start from right to left, i.e. from last index to index 0. This is beacuse for a current index i, we will need the information of whether dp[k] is True or False, where k > i.
- Trie determines whether a substring is a dictionary word. DP determines whether that word can be combined with the remaining suffix to form a complete segmentation.


WORD-BREAK(s, wordDict)
- Build one trie using all words in wordDict.
- Intialize `dp[n] = True`, where n = len(s).
- Process starting indices i from n-1 down to 0.
- For each i, start at the Trie root and traverse using characters s[i], s[i+1] and so on.
- If no matching child exists for the next character, stop the traversal for this i.
- After each successful character match at index j, check current node 's end-of-word flag.
    - If it is `True`, check `dp[j+1]`.
        - If `dp[j+1]` is `True`, set `dp[i] = True` and stop the traversal for this i.
        - Otherwise, continue searching for a longer matching word, if possible.
- return `dp[0]`


Python Code :
```python
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

def wordBreak(s, wordDict):
    # Build Trie
    trie = Trie()
    for word in wordDict:
        trie.insert(word)
    node = trie.root
    
    # initialize the dp array
    n = len(s)
    dp = [True] * n
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[j] in root.children: # is the current character the child of the current node?
                node = node.chidren[s[j]] # if yes, then traverse to the child
                if node.end_of_word = True :
                    if dp[j+1] == True: # checking if the remaining suffix is segmentable or not.
                        dp[i] = True
                        break
            else :
                break # if not, then stop traversing for that i

# There are many flaws in above wordBreak
# 1. DP initilization is correct. The length of array should be (n+1). Also, only the value at index n should be initialized to `True`, and rest should be initialized to `False`.
# 2. Need to reset node for every starting index i.  The `node = trie.root` should be moved to begining of outer loop.
# 3. Currently, I am checking s[j] in root.children. I should check in node.children.
# 4. Typo in `node = node.chidren[s[j]]`
# 5. This is assignment, not comparison `if node.end_of_word = True`.
# 6. Missing return statement. After both loops, return dp[0].

def wordBreak(s, wordDict):
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
                if node.end_of_word = True :
                    if dp[j+1] == True: # checking if the remaining suffix is segmentable or not.
                        dp[i] = True
                        break
            else :
                break # if not, then stop traversing for that i
            
```
