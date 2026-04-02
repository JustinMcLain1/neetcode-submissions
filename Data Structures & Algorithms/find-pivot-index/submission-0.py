class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        #first calculate sum so we have the entire array
        #then initalize the left
        # iterate through the array
        #then calculate the right sum
        total = sum(nums)

        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            
            #this works because as you iterate the value
            #at that index subtracts from the total and adds
            #to the left index
            #this means eventually if there is a pivot index
            #then the right and left will eventually be greater
            #less than or equal to eachother
            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
        #there is no pivot index
        return -1


        #this is o(n) time complexity since we iterate
        #through the array once 
        #and constant time complexity because we only have
        #a few variables and arnt storing the array