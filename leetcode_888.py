'''
Easy problem.
Remember to use set here.
'''
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        total_A = sum(A)
        total_B = sum(B)
        
        target_of_B = set()
        for n in A:
            target_of_B.add(n-(total_A-total_B)//2)
        
        for n in B:
            if n in target_of_B:
                return [n+(total_A-total_B)//2, n]
