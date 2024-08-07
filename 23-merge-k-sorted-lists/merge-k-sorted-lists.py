class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0] 
        
        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
         
        return self.merge(left,right)
    
    def merge(self,l1,l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return dummy.next



    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
        
    #     mid = len(lists) // 2
    #     left = self.mergeKLists(lists[:mid])
    #     right = self.mergeKLists(lists[mid:])
        
    #     return self.merge(left, right)
    
    # def merge(self, l1, l2):
    #     dummy = ListNode(0)
    #     curr = dummy
        
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             curr.next = l1
    #             l1 = l1.next
    #         else:
    #             curr.next = l2
    #             l2 = l2.next
    #         curr = curr.next
        
    #     curr.next = l1 or l2
        
    #     return dummy.next