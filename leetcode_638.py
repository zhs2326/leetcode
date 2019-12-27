#This is my first version which leads to TLE.

	class Solution(object):
		def shoppingOffers(self, price, special, needs):
		
			def helper(needs):
				if needs == [0]*m:
					return 0

				res = float('inf')

				for i in range(m):
					needs[i] -= 1
					if needs[i] >= 0:
						res = min(res, helper(needs[:])+price[i])
					needs[i] += 1

				for sp in special:
					for i in range(len(needs)):
						needs[i] -= sp[i]
					if all(needs[i] >= 0 for i in range(len(needs))):
						res = min(res, helper(needs[:])+sp[-1])
					for i in range(len(needs)):
						needs[i] += sp[i]

				return res

			n = max(needs)+1
			m = len(needs)

			#call helper function to solve this problem recursively
			return helper(needs)
      
      
#Then I use memerization to avoid calculating the existed minimum price twice. This is version 2 which still leads to TLE.

class Solution(object):
	def shoppingOffers(self, price, special, needs):

		def helper(needs):
			if needs == [0]*m:
				return 0

			if tuple(needs) in d:
				return d[tuple(needs)]

			res = float('inf')

			for i in range(m):
				needs[i] -= 1
				if needs[i] >= 0:
					res = min(res, helper(needs[:])+price[i])
				needs[i] += 1

			for sp in special:
				for i in range(len(needs)):
					needs[i] -= sp[i]
				if all(needs[i] >= 0 for i in range(len(needs))):
					res = min(res, helper(needs[:])+sp[-1])
				for i in range(len(needs)):
					needs[i] += sp[i]

			d[tuple(needs)] = res
        
			return res


		n = max(needs)+1
		m = len(needs)

		d = {}

		#call helper function to solve this problem recursively
		return helper(needs)
    
    
#We can calculate the minimum price without special offers easily without recursion. This intuition leads to version 3 and it is accepted.

class Solution(object):
	def shoppingOffers(self, price, special, needs):

		def helper(needs):
			if needs == [0]*m:
				return 0

			if tuple(needs) in d:
				return d[tuple(needs)]

			res = 0

			for i in range(m):
				res += needs[i]*price[i]

			for sp in special:
				for i in range(len(needs)):
					needs[i] -= sp[i]
				if all(needs[i] >= 0 for i in range(len(needs))):
					res = min(res, helper(needs[:])+sp[-1])
				for i in range(len(needs)):
					needs[i] += sp[i]

			d[tuple(needs)] = res

			return res


		n = max(needs)+1
		m = len(needs)

		d = {}

		#call helper function to solve this problem recursively
		return helper(needs)
