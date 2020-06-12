'''
The follow up asks to solve it in O(nlogk), but actually it can be solved in O(n+klogk).
First we need a counter to count the frequency of all the words, which is an O(n) operation.
Then we can use quickselect to select the k most frequent words, which is an O(k) operation.
Last, we need to sort these k words, which is an O(klogk) operation.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        h = [(-v, k) for k, v in counter.items()]
        heapq.heapify(h)
        
        k_most_frequent = heapq.nsmallest(k, h)
        k_most_frequent.sort()
        
        return [k for (v, k) in k_most_frequent]

'''
Runtime: 52 ms, faster than 91.00% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 13.9 MB, less than 57.58% of Python3 online submissions for Top K Frequent Words.
'''
