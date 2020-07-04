class Solution:
    def convertToTitle(self, n: int) -> str:
        #number = A * 26 ^ 3 + B * 26 ^ 2 + C * 26 + D
        #number = [(A-'A')+1] * 26 ^ 3 + [(B-'A')+1] * 26 ^ 2 + [(C-'A')+1] * 26 + [(D-'A')+1]
        
        #(number-1) % 26 == D-'A'
        #((number-1) // 26 - 1) % 26 == C - 'A'
        #...
        
        title = []
        while n:
            n, remainder = (n - 1) // 26, (n - 1) % 26
            title.append(chr(ord('A') + remainder))
        
        return ''.join(title[::-1])
