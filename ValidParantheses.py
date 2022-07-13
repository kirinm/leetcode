class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        mySet = {')':'(',']':'[','}':'{' }
        for x in s:
            if x in mySet:
                top = myStack.pop() if myStack else '#'
                if mySet[x]!=top:
                    return False 
            else:
                myStack.append(x)
        if myStack:
            return False
        return True 