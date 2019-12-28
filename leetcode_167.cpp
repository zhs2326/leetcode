/*
Intuitively, there are three methods: hashmap, two pointers, binary search.
For this problem the two pointers approach is the best one.
Let's compare their time complexity and space complexity.

  Time complexity:
    1. hashmap: O(n)
    2. two pointers: O(n)
    3. binary search: O(nlogn)      For every number, it takes logn to find its possible target with binary search.
   
  Space complexity:
    1. hashmap: O(n)
    2. two pointers: O(1)
    3. binary search: O(1)
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int p1 = 0;
        int p2 = numbers.size()-1;
        
        while (p1 < p2){
            if(numbers[p1]+numbers[p2] < target){
                p1 ++;
            }else if(numbers[p1]+numbers[p2] > target){
                p2 --;
            }else{
                break;
            }
        }
        
        return {p1+1, p2+1};
    }
};
