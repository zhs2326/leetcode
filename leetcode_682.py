#This is a good problem to test your understanding of stack.
#Just write your code according to the description of the problem. 

class Solution(object):
	def calPoints(self, ops):
		"""
		:type ops: List[str]
		:rtype: int
		"""

		stack = []
		res = 0

		for i in range(len(ops)):
			if ops[i] == 'C':
				res -= stack[-1]
				stack.pop()
			elif ops[i] == 'D':
				res += stack[-1]*2
				stack.append(stack[-1]*2)
			elif ops[i] == '+':
				res += stack[-1]+stack[-2]
				stack.append(stack[-1]+stack[-2])
			else:
				res += int(ops[i])
				stack.append(int(ops[i]))

		return res
