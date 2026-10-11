## Trie
- First lets understand, What is Trie ? 
    - Trie is a tree, built of all the words of wordDict.
    - In trie, each node (except the root node) represents a character and path from the root represents prefixes of words.
    - A branch in the tree diverge, when the two words stop having the same prefixes.
    - A full complete path from root represents a word in wordDict.
    - Also :
        - Trie need not be a binary tree.
        - The root node can have 1 node, 2 node or more than 2 node. This is true for all other non-root nodes too.
        - A root can have maximum of 26 nodes, for each english alphabet letters (assuming that only either lower/upper case letters are allowed).
- What does each node in a trie contain? 
- Conceptually, each node contains :
    1. Children : links to the next character nodes.
    2. End-of-words-flag : Indicates whether a word ends at this node?

