#A very interesting problem. The solution is strongly recommended!

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                p1 = i
                break
        else:
            return 0
        
        
        mi = float('inf')
        for i in range(p1, len(nums)):
            if nums[i] < mi:
                p1 = i
                mi = nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            if j < len(nums)-1 and nums[j] > nums[j+1]:
                p2 = j
                break
        
        ma = float('-inf')
        for j in range(p2, -1, -1):
            if nums[j] > ma:
                p2 = j
                ma = nums[j]
        
        
        for i in range(len(nums)):
            if nums[i] > nums[p1]:
                p1 = i
                break
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] < nums[p2]:
                p2 = j
                break
        
        return p2-p1+1
        
