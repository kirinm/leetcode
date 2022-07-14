class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        rightList = [0]*size
        leftList = [0]*size
        leftList[0]=height[0]
        rightList[size-1]=height[size-1]
        ans=0
        for i in range(1,size):
            leftList[i]=max(leftList[i-1],height[i])
        for i in reversed(range(0,size-1)):
            rightList[i]=max(rightList[i+1],height[i])
        for i in range(1,size):
            ans+=min(rightList[i],leftList[i])-height[i]
        return ans



        