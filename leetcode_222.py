'''
The easiest way is to iterate over all the nodes in the tree. 

However, we need to take care that the tree is a complete one.
Therefore, except the last level, we can calculate the number of nodes in each level easily.
suppose we have a complete tree with depth = d, then the number of nodes except the last level is: 2**d-1
Therefore, the question remained is just how to know the number of nodes in the last level.

Here we can use binary search to solve the problem.
The idea is easy: just like ordinary binary search, we get the mid point and check whether there is a node in the last level 
at the mid point.
If there is one, we set left = mid+1, and continue binary search.
Likewise, if there isn't one, we set right = mid-1, and continue binary search.
Doing these steps until we have found the last node in the last level.
And then we can get the total number of nodes in the tree easily.

Time Complexity: O(d)^2
Space Complexity: O(1)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(pivot, root, d):
            l = 0
            r = 2**d-1
            
            for i in range(d):
                mid = l+(r-l)//2
                if pivot <= mid:
                    r = mid
                    root = root.left
                else:
                    l = mid+1
                    root = root.right
            
            return root
            
        
        if not root:
            return 0
        
        #compute the depth here
        d = -1
        node = root
        
        while node:
            d += 1
            node = node.left
            
        #binary search to find the number of nodes in the last level
        res = 0
        l = 0
        r = 2**d-1
        
        while l <= r:
            mid = l+(r-l)//2
            #call helper function here
            if helper(mid, root, d):
                print mid
                res = mid
                l = mid+1
            else:
                r = mid-1
        
        return 2**d+res
