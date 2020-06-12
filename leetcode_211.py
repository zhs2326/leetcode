'''
A typical problem with Trie.
The tricky part is that you not only should have a good command of Trie but also should fully understand recursive methods.
'''

class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.isWord = False 
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trietree = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trietree
        for c in word:
            node = node.children[c]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, node):
            if not word and node.isWord:
                return True
            for i, c in enumerate(word):
                if c == '.':
                    for child in node.children:
                        if helper(word[i+1: ], node.children[child]):
                            return True
                    return False
                else:
                    if c in node.children:
                        return helper(word[i+1: ], node.children[c])
                    else:
                        return False
        
        return helper(word, self.trietree)
