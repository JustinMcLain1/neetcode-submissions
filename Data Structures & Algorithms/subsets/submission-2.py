class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         
        result = []
         
        subset = []
        
        def DFS(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            DFS(i+1)
            subset.pop()
            DFS(i+1)
        
        DFS(0)
        return result
