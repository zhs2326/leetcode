#Interestring question!
#The solution to such kind of questions is summarized as below:
#(1)  if we want to realize randX with randY, where Y > X.
#     In such cases, it's very simple.
#     while True:
#       rand_num = randY()
#       if rand_num <= X:
#         return rand_num
#(2)  if we want to realize randX with randY, where Y < X.
#     In such cases, we need to realize randZ first, where Z >= X and Z-1 = Y**k*(Y-1) + Y**(k-1)*(Y-1) + ... + Y-1
#     In general, we should find the smallest Z that satisfies the requirement above.
#     Then the following implementation is the same as the first case.


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            uniform_distribution = 7 * (rand7() - 1) + rand7() - 1
            if uniform_distribution < 40:
                break
        
        return uniform_distribution // 4 + 1
