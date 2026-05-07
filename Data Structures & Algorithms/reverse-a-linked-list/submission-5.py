class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        self.prev = None
        self.curr = head
        
        while self.curr != None:
            temp = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = temp

        return self.prev
        # 0 1 2 3 4 

        #self.prev = None
        #self.curr = head

        # while self.curr != None:
        #    temp = self.curr.next # temp = 1 then temp = 2 3 4 None
        #    self.curr.next = self.prev #next = 0 next = 1 2 3 4
        #    self.prev = self.curr # prev = 0 prev = 1 2 3 4
        #    self.curr = temp # curr = 1 curr = 2 3 4 None Break

            # 1 0 2 3 4
            
            # 2 1 0 3 4

            # 3 2 1 0 4

            # 4 3 2 1 0