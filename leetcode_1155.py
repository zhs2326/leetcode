'''
A typical DP problem. 
Note that for the recursion solution, you need to do it with memo. (Otherwise your solution will time out.)
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        pre_dp = {0: 1}
        curr_dp = collections.defaultdict(int)
        
        for i in range(d):
            for j in range(1, f+1):
                for point, count in pre_dp.items():
                    curr_dp[point+j] += count
            pre_dp = curr_dp
            curr_dp = collections.defaultdict(int)
        
        return pre_dp[target]%(10**9+7)
