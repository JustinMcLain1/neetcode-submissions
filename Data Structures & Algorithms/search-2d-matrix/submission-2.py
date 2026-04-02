class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        #this checks while bot row is not moved past top
        while top <= bot:
            #grab the middle row
            row = (top + bot) //2
            #if the target is greater than the highest value in the row
            #then we move the top down one
            if target > matrix[row][-1]:
                top = row + 1
            #otherwise move the bottom up one row
            elif target < matrix[row][0]:
                bot = row - 1
            #if the target is inbetween the start and end values 
            #we know we its in the current row and can leave the while loop
            else:
                break
        
        #if the bottom row iterates past the top then return false
        if not (top <= bot):
            return False
        row = (top + bot) //2
        #grab first index and last index
        l,r = 0, COLS - 1
        #regular binary search
        while l <= r:
            m = (l+r) //2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False