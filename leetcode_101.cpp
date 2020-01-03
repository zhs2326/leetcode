/*
Recursion is the first method that you should come up with when solving problems related to trees.
A tricky part of this problem is that for the root you should use it twice as the two parameters of the helper function.
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
    bool helper(TreeNode *root1, TreeNode *root2){
        if(root1 == NULL && root2 == NULL){
            return true;
        }else if(root1 != NULL && root2 != NULL){
            if(root1->val != root2->val){
                return false;
            }
            bool res = helper(root1->left, root2->right) && helper(root1->right, root2->left);
            return res;
        }else{
            return false;
        }
    }
    bool isSymmetric(TreeNode* root) {
        return helper(root, root);
    }
};
