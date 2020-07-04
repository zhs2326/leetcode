class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        p1, p2 = 0, 0
        
        while p1 < len(start) and p2 < len(end):
            while p1 < len(start) and start[p1] == 'X':
                p1 += 1
            while p2 < len(end) and end[p2] == 'X':
                p2 += 1
            if p1 < len(start) and p2 < len(end) and (start[p1] != end[p2] or start[p1] == 'L' and p1 < p2 or start[p1] == 'R' and p1 > p2) or p1 < len(start) and p2 == len(end) or p1 == len(start) and p2 < len(end):
                return False
            else:
                p1 += 1
                p2 += 1
        
        while p1 < len(start):
            if start[p1] == 'L' or start[p1] == 'R':
                return False
            p1 += 1
            
        while p2 < len(end):
            if end[p2] == 'L' or end[p2] == 'R':
                return False
            p2 += 1
        
        return True
