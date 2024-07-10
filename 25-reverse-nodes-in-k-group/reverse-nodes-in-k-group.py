# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(None, head)
        dummy = start

        def getKthNode(node,k):
            while k>0:
                node = node.next
                if node is None:
                    return
                k-=1
            return node
        
        while True:
            kNode =  getKthNode(dummy,k)
            if not kNode:
                break
            
            kNodeNext = kNode.next

            prev, curr = kNode.next, dummy.next

            while curr!=kNodeNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp2 = dummy.next
            dummy.next = kNode
            dummy = tmp2
        return start.next
             
        # start = ListNode(None, head)
        # groupPrev = start
        # def getKthNode(node, k):
        #     while  k > 0:
        #         node = node.next
        #         if node is None:
        #             return
        #         k-=1
        #     return node
        # while True:
        #     kNode = getKthNode(groupPrev, k)
        #     if not kNode: break
        #     groupNext = kNode.next
             
        #     #for reversing order
        #     prev, curr = kNode.next, groupPrev.next

        #     while curr != groupNext:
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp
        #     temp2 = groupPrev.next # group prev must point to start of next group
        #     groupPrev.next = kNode 
        #     groupPrev = temp2
        # return start.next
        