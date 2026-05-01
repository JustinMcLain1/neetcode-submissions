class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        
        for op in operations:
            if op == 'C':
                total.pop()
            elif op == 'D':
                total.append(2 * total[-1])
            elif op == '+':
                total.append(total[-1] + total[-2])
            else:
                total.append(int(op))
        
        return sum(total)


