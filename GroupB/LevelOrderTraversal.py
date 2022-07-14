# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            q = [root]
            if not root: return []
            result = []
            while q:
                lenq = len(q)
                layer = []
                for i in range(lenq):
                    curr = q.pop(0)
                    layer.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                result.append(layer)
            return result 
            
                
            
        