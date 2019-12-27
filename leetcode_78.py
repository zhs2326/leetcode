#We can solve this problem recursively.
#Namely, for a list nums with elements nums[0: len(nums)]
#we can first find the subsets of nums[0: len(nums)-1], we call it res
#then the subsets of nums is res+[temp+[nums[-1]] for temp in res]
#and the base case is when the list becomes empty
#then the subset of an empty list is an empty list

class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def helper(nums):
			if not nums:
				self.res.append([])
				return
			helper(nums[:-1])

			self.res += [temp+[nums[-1]] for temp in self.res]


		self.res = []

		helper(nums)

		return self.res
