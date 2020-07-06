class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        first_half, second_half = lists[:len(lists)//2], lists[len(lists)//2:]
        first_half_sorted, second_half_sorted = self.mergeKLists(first_half), self.mergeKLists(second_half)
        
        dummy = ListNode()
        p1, p2 = first_half_sorted, second_half_sorted
        p = dummy
        
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        
        return dummy.next
