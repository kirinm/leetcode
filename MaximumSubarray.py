class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNums = nums[0]
        total = 0 
        for n in nums:
            if total < 0:
                total = 0
            total+=n
            maxNums = max(maxNums,total)
        return maxNums 
            