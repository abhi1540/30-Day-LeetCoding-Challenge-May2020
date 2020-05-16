    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        evenhead = even
        
        while even is not None and even.next is not None:
            
            #print(odd.val,even.val)
            odd.next = odd.next.next
            even.next = even.next.next       
            odd = odd.next
            even = even.next
            
        odd.next = evenhead

        return head