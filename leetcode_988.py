'''
Just use DFS with backtracking. Nothing special here.
'''

class Solution:
    def __init__(self):
        self.smallest = chr(ord('z')+1)
    
    def recursive_find_smallest_string_from_leaf(self, node, curr):
        if not node.left and not node.right:
            curr.append(chr(node.val+ord('a')))
            string_from_leaf = (''.join(curr))[::-1]
            self.smallest = min(self.smallest, string_from_leaf)
            curr.pop()
            return
        
        curr.append(chr(node.val+ord('a')))
        if node.left:
            self.recursive_find_smallest_string_from_leaf(node.left, curr)
        if node.right:
            self.recursive_find_smallest_string_from_leaf(node.right, curr)
        curr.pop()
        
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.recursive_find_smallest_string_from_leaf(root, [])
        
        return self.smallest
