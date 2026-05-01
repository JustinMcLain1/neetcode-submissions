class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        ops = [x.upper() for x in operations]

        for i in ops:
            if i == 'C':
                total.pop()
            elif i == 'D':
                total.append(2 * total[-1])
            elif i == '+':
                new = total[-1] + total[-2]
                total.append(new)
            else:
                total.append(int(i))
        
        return sum(total)



