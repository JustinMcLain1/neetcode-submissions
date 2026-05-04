class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        self.prev = None
        self.curr = head
        if head == None:
            return None
        
        while self.curr != None:
            temp = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = temp

        return self.prev