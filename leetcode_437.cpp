/*
An interesting question.
It's not difficult for us to figure out a recursion method with map to achieve the O(n) time complexity.
One thing that might inspire you is that there are some similarities between this problem and the one to find maximum sum of
consecutive subarrays in an array.
In both problem we can utilize the cummulative sum to calculate the sum of subpath(subarray) more conveniently.
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
    unordered_map<int, int> umap;
    int target;
    
    int helper(TreeNode* root, int currSum){
        currSum += root->val;
        
        int res = 0;
        res += umap[currSum-target];
        umap[currSum]++;
        
        int left = 0;
        int right = 0;
        
        if(root->left){
            left = helper(root->left, currSum);
        }
        if(root->right){
            right = helper(root->right, currSum);
        }
        
        umap[currSum]--;
        
        return res+left+right;
    }
    
    int pathSum(TreeNode* root, int sum) {
        if(!root){
            return 0;
        }
        
        target = sum;
        umap[0] = 1;
        
        return helper(root, 0);
    }
};
