class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = [[] for n in range(len(nums)+1)]
        count = {}
        res = []
        for n in nums:
            count[n]=count.get(n,0)+1
        #{1:3,2:2,3:1}
        for c,v in count.items():
            freq[v].append(c)
        #[[],[3],[2],[1],[],[],[]]
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
            if len(res)==k:
                return res