class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElem = 0
        myDict = {}
        output = 0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]]=1
            else:
                myDict[nums[i]]+=1
        for i in myDict:
            if myDict.get(i) > majElem:
                majElem = myDict.get(i)
                output = i 
        return output


            
        