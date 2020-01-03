/*
An easy problem. 
Here's the dfs method with recursion.
The bfs method and the dfs method with stack will be updated later.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int res = 0;
    
    void helper(TreeNode *root, int depth){
        if(root == NULL){
            return;
        }else{
            depth ++;
            res = max(res, depth);
            helper(root->left, depth);
            helper(root->right, depth);
        }
        
    }
    
    int maxDepth(TreeNode* root) {
        helper(root, 0);
        return res;
    }
};
