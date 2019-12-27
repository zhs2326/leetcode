'''
This problem is a good one to test your understanding of sliding window.
Since all the elements in this array are positive,
when we find the sum of the sliding window is less than the target,
we just increase the end pointer.
When we find the sum of the sliding window is greater than the target,
we should increase the start pointer.
So we can use this method to find all the possible subarrays and return the one with the minimum length.
The time complexity is O(n), where n is the length of the array.
Moreover, since we need to find the subarray with the minimum length,
if we've already find a subarray whose sum of elements is greater than or equal to the target,
there is no need for us to consider these subarrys with longer length.
But this only makes a subtle difference.
'''

#version 1
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        p1 = p2 = 0
        sum = 0
        res = float('inf')
        
        while p2 < len(nums):
            sum += nums[p2]
            if sum >= s:
                res = min(res, p2-p1+1)
            
            while p1 < p2 and sum >= s:
                p1 += 1
                sum -= nums[p1-1]
                if sum >= s:
                    res = min(res, p2-p1+1)
                else:
                    break
                    
            p2 += 1
        
        if res == float('inf'):
            return 0
        else:
            return res
            
            
        
#version2        
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        p1 = p2 = 0
        sum = 0
        res = float('inf')
        
        while p2 < len(nums):
            sum += nums[p2]
            if sum >= s:
                res = p2-p1+1
            
            while p1 < p2 and sum >= s:
                p1 += 1
                sum -= nums[p1-1]
                if sum >= s:
                    res = p2-p1+1
                else:
                    break  
                    
            p2 += 1                       
            if res != float('inf'):       #no need to check sublist with length greater than res
                p1 += 1
                sum -= nums[p1-1]
                
        
        if res == float('inf'):
            return 0
        else:
            return res
            
            
        
