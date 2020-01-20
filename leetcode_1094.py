'''
Similar question as meeting room series.
For such problem, sort first and then use your logic! :)
'''
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        trips1 = sorted(trips, key = lambda x: x[1])
        trips2 = sorted(trips, key = lambda x: x[2])
        
        total = 0
        
        p1 = p2 = 0
        
        while p1 < len(trips):
            while max(p1, p2) < len(trips) and trips1[p1][1] < trips2[p2][2]:
                total += trips1[p1][0]
                if total > capacity:
                    return False
                p1 += 1
            while max(p1, p2) < len(trips) and trips2[p2][2] <= trips1[p1][1]:
                total -= trips2[p2][0]
                p2 += 1
        
        return True
        
