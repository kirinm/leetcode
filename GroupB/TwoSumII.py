class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1
        while l < r:
            s = numbers[l]+numbers[r]
            if s > target:
                r-=1
                continue
            if s < target:
                l+=1
                continue
            else:
                return [l+1,r+1]