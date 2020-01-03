#The intuition of that we should try to find two segments of subarrays that their length plus the possible 0 between is the
#maximum one. Like this: 111110111111111
#It's not difficult for us to implement this idea. Everytime when we meet a zero, we should update the length of these two
#subarrays.
#However, there are some tricky parts that we should take care of.
#Firstly, when we reach the end of the array, we should update the maximum length again because there is no 0 afterwards.
#Secondly, it's likely that the whole array only contains 1, in which case we have no 0 to utilize. So we need to check whether
#there is 0 in the array. If that's true, it means that we have 0 to utilize and we should add the result by 1.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_length = 0
        prev = 0
        curr = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 1
                max_length = max(max_length, prev+curr)
                prev = curr
                curr = 0
            else:
                curr += 1
        max_length = max(max_length, prev+curr)
        
    
        return max_length+count
