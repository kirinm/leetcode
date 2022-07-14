class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = { i:[] for i in range(numCourses)} 
        
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        #visitset will store all courses along current dfs path
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
                #detected a loop
                
            if preMap[crs] == []:
                return True
            #no prereqs
            
            visiting.add(crs)
            for pre in preMap[crs]:
                #if 1 course cant be completed then return false for whole function
                if not dfs(pre): return False
            visiting.remove(crs)
            #finished visiting it
            
            #since we know it can be visited we can set it to an empty list 
            preMap[crs] = []
            return True
        
        #if graph isn't fully connected 
        for c in range(numCourses):
            if not dfs(c): return False
        return True