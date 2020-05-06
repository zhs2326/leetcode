#When I see this problem, my first intuition is that we shouldn't use bfs for the insert part. Otherwise, we aren't fully
#utilize the complete property. So I keep track of the number of nodes in the tree, and do insert based on this number, which
#is an O(logn) operation.
#By the way, lee215's solution is really interesting!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.num_of_nodes = 0
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.pop()
            self.num_of_nodes += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        index = self.num_of_nodes+1
        parent = self.root
        
        #convert index to binary
        res = ''
        while index:
            index, remainder = index//2, index%2
            res = str(remainder)+res
        res = res[1:]
        
        node = self.root
        while res != '':
            if len(res) == 1:
                parent = node
            left_or_right = int(res[0])
            res = res[1:]
            if left_or_right:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(v)
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(v)
        
        self.num_of_nodes += 1
        
        return parent.val
        

    def get_root(self) -> TreeNode:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
