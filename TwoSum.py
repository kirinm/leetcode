class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #number:position 
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [i,seen[comp]]
            else:
                seen[nums[i]]=i