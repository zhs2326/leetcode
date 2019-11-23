'''
Apparently, we can solve this problem recursively.

Given a node, first we need to check whether this node should be deleted.
If that's true, than we can go on to its children.
If that's not true, than we need to determine whether this node is a root node.

So here we can use a flag to indicate that.
If this node is a root node, then first we should add that node to the result.
Second, we should process its children and set the flag to be False.
If this node isn't a root node, then we just go to its children and set the flag to be False.

Time complexity: O(MN)   N is the number of nodes, M is the length of to_delete
Space complexity: O(H)   Because we will need a stack to solve this problem recursively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        def helper(root, to_delete, first):
            if not root:
                return
            if root.val not in to_delete:
                if first:
                    self.res.append(root)
                root.left = helper(root.left, to_delete, False)
                root.right = helper(root.right, to_delete, False)
                return root
            else:
                to_delete.remove(root.val)
                root.left = helper(root.left, to_delete, True)
                root.right = helper(root.right, to_delete, True)
                return None
                
                
        #the key point is that we need to determine whether one node is the root
        
        if not root:
            return []
        
        self.res = []
        
        #call helper function here
        helper(root, to_delete, True)
        
        return self.res
