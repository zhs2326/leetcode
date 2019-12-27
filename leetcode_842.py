#There are several cases that we should take into consideration.

#No leading zeros except zero itself.

#The numbers should be less than 2^31.

 class Solution(object):
 	def splitIntoFibonacci(self, S):
 		"""
 		:type S: str
 		:rtype: List[int]
 		"""
 		def helper(S, temp):
 			if self.res:
 				return
 			if not S and len(temp)>2:
 				self.res =  temp
 				return
 			for i in range(len(S)):
 				if S.startswith('0') and i > 0:
 					break
 				if int(S[:i+1]) > 2**31-1:
 					break
 				if len(temp) < 2 or (len(temp) >= 2 and int(S[:i+1]) == int(temp[-1])+int(temp[-2])):
 					temp.append(S[:i+1])
 					helper(S[i+1:], temp[:])
 					temp = temp[:-1]


 		if not S:
 			return None

 		self.res = None
 		helper(S, [])

 		return self.res
