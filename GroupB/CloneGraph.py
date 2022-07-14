"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            # if the node is already cloned, return the node
            if not node: 
                return None
            if node in oldToNew:
                return oldToNew[node]
            
            # actual clone step
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # create edge (adjacency list) for this node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) 