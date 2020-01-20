'''
A very interesting problem!
The intuition is suppose we have a number n
  (1) if n can be divided by 2, then the minimum operation is: the result of n/2 + 1(copy) + 1(paste)
  (2) if n can be divided by 3, then the minimum operation is: the result of n/3 + 1(copy) + 2(paste)
  ...
  ...
  (n-1) if n can be divided by n, then the minimum operation is: the result of n/n(0) + 1(copy) + n-1(paste)
  
With this intuition in mind, this problem can be easily solved with recursion.
'''

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 0
        for i in range(2, n+1):
            if n % i == 0:
                temp = self.minSteps(n/i)
                break
        res = 1+temp+(i-1)
        return res
