#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    # DFS
    # def __init__(self) -> None:
    #     self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        # DFS
        # if not node:
        #     return node
        
        # if node in self.visited:
        #     return self.visited[node]

        # clone_node = Node(node.val, [])

        # self.visited[node] = clone_node

        # if node.neighbors:
        #     clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        # return clone_node       
        # 

        # BFS
        if not node:
            return node

        visited = {}

        queue = deque([node]) 
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]
        
# @lc code=end

