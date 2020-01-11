#We only need to take care of the relative order of letters in S.
#From my point of view, this problem should be classified as an easy one.

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        ds = {}
        
        for i in range(len(S)):
            ds[S[i]] = i
        
        dt = collections.Counter(T)
        
        res = [""]*27
        
        for k in dt:
            if k in ds:
                res[ds[k]] = k*dt[k]
            else:
                res[26] += k*dt[k]
        
        return ''.join(res)
        
        
        
