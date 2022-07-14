class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if target == nums[mid]:
                return mid
            
            if nums[l]<=nums[mid]:
                if nums[mid]<target:
                    l=mid+1
                elif nums[l] > target:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[mid]>target:
                    r=mid-1
                elif nums[r]<target:
                    r=mid-1
                else:
                    l=mid+1
        return -1