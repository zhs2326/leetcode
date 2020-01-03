#We can use a recursion method to solve this problem.
#If the left subtree of a node only contains 0, we delete it(set the left pointer to NULL).
#Likewise, if the right subtree of a given node only contains 0, we also delete it(set the right pointer to NULL).
#IF both the left subtree and right subtree of a given node only contains 0, now we need to check whether the value of the
#node itself is 0 or not. IF its value is 0, we should also delete this node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root.left and not root.right:
            return root.val == 0
        
        left_bool = True
        right_bool = True
        
        if root.left:
            left_bool = self.helper(root.left)
        if root.right:
            right_bool = self.helper(root.right)
        if left_bool and right_bool:
            root.left = None
            root.right = None
            return root.val == 0
        elif left_bool:
            root.left = None
            return False
        elif right_bool:
            root.right = None
            return False
        else:
            return False
    
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root
        
