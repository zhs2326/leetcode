'''
We can use two helper functions to solve this problem.
Here, the first helper function solve achieves just the same goal of the problem itself, namely finding the minimum number of operations to make the binary representation zero.
The second helper function convert aims to convert a binary representation into the form like '10000...', which starts with one '1' and ends with zero or mutiple consecutive '0's.
In addition, two dicts are used to realize memoization.
'''

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        s = bin(n)[2: ]
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        return self.solve(s, d1, d2)
    
    def solve(self, s, d1, d2):
        if not s:
            return 0
        if s in d1:
            return d1[s]
        
        if s[0] == '1':
            if len(s) >= 2:
                new_s = '1' + '0' * (len(s) - 2)
            else:
                new_s = ''
            res = 1 + self.convert(s[1: ], d1, d2) + self.solve(new_s, d1, d2)
        else:
            res = self.solve(s[1: ], d1, d2)
        
        d1[s] = res
            
        return res
    
    def convert(self, s, d1, d2):
        if not s:
            return 0
        if s == '1':
            return 0
        if s == '0':
            return 1
        if s in d2:
            return d2[s]
        
        if s[0] == '1':
            res = self.solve(s[1: ], d1, d2)
        else:
            if len(s) >= 2:
                new_s = '1' + '0' * (len(s) - 2)
            else:
                new_s = ''
            res = 1 + self.convert(s[1: ], d1, d2) + self.solve(new_s, d1, d2)
            
        d2[s] = res

        return res
