#This problem can be easily solved with recursion.
#But the problem itself lacks logic.

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root.left and not root.right:
                return "("+str(root.val)+")"
            
            if root.left:
                res_left = helper(root.left)
            else:
                res_left = "()"
            
            if root.right:
                res_right = helper(root.right)
            else:
                res_right = ""
            
            return "("+str(root.val)+res_left+res_right+")"
        
        if not t:
            return ""
        
        res = helper(t)
        
        return res[1: -1]
