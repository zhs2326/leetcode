'''
It's not difficult to find out that this problem can be solved with Trie.
One thing noteworthy is that for the input like ['cat', 'cats', 'dog', 'catsdog'],
even though 'catsdog' can't be constructed by 'cat' + anything, it can be constructed by 'cats' and 'dog',
thus we need to do something like backtracking here.
'''
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        def search_helper(node, word):
            if not word:
                return True
            
            root = node
            
            for i, c in enumerate(word):
                if c not in node.children:
                    return False
                node = node.children[c]
                if node.is_word:
                    if search_helper(root, word[i+1: ]):
                        return True
            
            return False
        
        words.sort(key=lambda x: len(x))
        trietree = Trie()
        res = []
        
        for word in words:
            #search first
            if search_helper(trietree.root, word) and word:
                res.append(word)
            #then insert
            trietree.insert(word)
        
        return res
            
                
        
        
