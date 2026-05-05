class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #count = Counter(students) #{"1" : 2, "0": 2} depends on input
        #leftOver = len(students) #4
        #
        #for sandwich in sandwiches:
        #    if count[sandwich] > 0: 
        #        count[sandwich] -=1
        #        leftOver -= 1
        #    else:
        #        break
        #
        #return leftOver

        queue = deque(students)
        sandwiches_index = 0
        
        attempts = 0
        while queue and attempts < len(queue):
            student = queue.popleft()
            if student == sandwiches[sandwiches_index]:
                sandwiches_index += 1
                attempts = 0  # Reset since someone ate
            else:
                queue.append(student)
                attempts += 1  # Track consecutive failures
        
        return len(queue)