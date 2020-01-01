/*
An interesting question.
We need a hashtable which stores the count and the index of the first occurance of every letter.
I write an one-pass solution, which I learn from lee215's code.(https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC%2B%2BPython-One-Pass-Solution)
*/

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, pair<int, int>> umap;
        int maxCount = 0;
        int res = INT_MAX;
        for(int i = 0; i < n; i++){
            umap[nums[i]].first++;
            if (umap[nums[i]].first == 1){
                umap[nums[i]].second = i;
            }
            if (umap[nums[i]].first > maxCount){
                res = i-umap[nums[i]].second+1;
                maxCount = max(maxCount, umap[nums[i]].first);
            }else if(umap[nums[i]].first == maxCount){
                res = min(res, i-umap[nums[i]].second+1);
            }
        }
        
        
        return res; 
        
    }
};
