"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            if node and node not in clone:
                clone[node] = Node(node.val, [])
                clone[node].neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return clone.get(node)

        clone = {}
        return dfs(node)
    

"""
Use DFS to clone the neighbors of the node.
Time complexity: O(N + E), N is number of node, E is number of edges.
Space complexity: O(N)
"""
