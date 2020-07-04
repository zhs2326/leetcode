class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        permutations = collections.deque([''])
        for i, c in enumerate(S):
            if c.isalpha():
                length = len(permutations)
                for j in range(length):
                    string = permutations.popleft()
                    permutations.append(string+c.upper())
                    permutations.append(string+c.lower())
            else:
                for j in range(len(permutations)):
                    permutations[j] += c
        
        return permutations
        
