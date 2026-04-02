class Deque:
    
    def __init__(self):

        self.curr = []

    def isEmpty(self) -> bool:
        
        if self.curr:
            return False
        return True

    def append(self, value: int) -> None:
        
        self.curr.append(value)

    def appendleft(self, value: int) -> None:
        
        self.curr.insert(0, value)

    def pop(self) -> int:
        
        if self.curr:
            return self.curr.pop()
        else:
            return -1

    def popleft(self) -> int:
        
        if self.curr:
            return self.curr.pop(0)
        else:
            return -1