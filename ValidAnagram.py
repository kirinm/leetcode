class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        for x in s:
            s_set[x]=s_set.get(x,0)+1
        for x in t:
            t_set[x]=t_set.get(x,0)+1
        return s_set == t_set 
            