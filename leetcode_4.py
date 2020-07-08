'''
IMO, it's a hard hard problem.
However, you must try to solve it since it's very common in the interview. 
'''

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		left, right = 0, len(nums1)
		half_length = (len(nums1)+len(nums2))//2

		while left <= right:
			mid = left+(right-left)//2
			nums1_first_half, nums1_second_half = nums1[:mid], nums1[mid:]
			nums2_first_half, nums2_second_half = nums2[:half_length-mid], nums2[half_length-mid:]

			nums1_first_half_max = nums1_first_half[-1] if nums1_first_half else float('-inf')
			nums1_second_half_min = nums1_second_half[0] if nums1_second_half else float('inf')

			nums2_first_half_max = nums2_first_half[-1] if nums2_first_half else float('-inf')
			nums2_second_half_min = nums2_second_half[0] if nums2_second_half else float('inf')

			if nums1_first_half_max <= nums2_second_half_min and nums2_first_half_max <= nums1_second_half_min:
				if (len(nums1)+len(nums2))%2 == 0:
					return (max(nums1_first_half_max, nums2_first_half_max)+min(nums1_second_half_min, nums2_second_half_min))/2
				else:
					return min(nums1_second_half_min, nums2_second_half_min)
			elif nums1_first_half_max > nums2_second_half_min:
				right = mid-1 
			else:
				left = mid+1
